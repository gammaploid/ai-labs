#!/usr/bin/env python3
"""
Chat Log Parser for LaTeX Appendix

This scr                # Add accumulated content before the copilot response
                if current_block:
                    content = '\n'.join(current_block).strip()
                    if content:
                        output_lines.append(content)
                output_lines.append('\\end{userprompt}')
                output_lines.append('')
                current_block = []
                in_user_prompt = False
            
            # Start new LLM response
            output_lines.append('\\begin{llmresponse}')
            output_lines.append(line)
            in_llm_response = True
            current_block = [] logs and converts them into properly formatted LaTeX
userprompt and llmresponse tcolorbox environments.

Logic:
- When encountering "gammaploid: " -> start a \begin{userprompt}
- When encountering "GitHub Copilot:" -> end userprompt, start \begin{llmresponse}  
- Continue until next "gammaploid: " -> end llmresponse, start new userprompt
- Sanitize LaTeX special characters and markdown syntax

Usage:
    python parse_chat_logs.py input_file.txt output_file.tex
"""

import re
import sys
import argparse

def sanitize_latex(text):
    """
    Keep text simple - no escaping, just return as-is for clean output.
    """
    return text

def parse_chat_logs(input_text):
    """
    Parse chat logs and return formatted LaTeX.
    
    Args:
        input_text (str): Raw chat log content
        
    Returns:
        str: Formatted LaTeX with userprompt/llmresponse environments
    """
    output_lines = []
    current_block = []
    in_user_prompt = False
    in_llm_response = False
    
    lines = input_text.split('\n')
    
    for line in lines:
        stripped_line = line.strip()
        
        # Check for user prompt start
        if stripped_line.startswith('gammaploid:'):
            # End previous llm response if active
            if in_llm_response:
                # Add accumulated content
                if current_block:
                    content = '\n'.join(current_block).strip()
                    if content:
                        output_lines.append(content)
                output_lines.append('\\end{llmresponse}')
                output_lines.append('')
                current_block = []
                in_llm_response = False
            
            # Start new user prompt
            output_lines.append('\\begin{userprompt}')
            output_lines.append(line)
            in_user_prompt = True
            current_block = []
            
        # Check for LLM response start
        elif stripped_line.startswith('GitHub Copilot:'):
            # End previous user prompt if active
            if in_user_prompt:
                # Add any accumulated content before the copilot response
                if current_block:
                    content = '\n'.join(current_block).strip()
                    if content:
                        output_lines.append(sanitize_latex(content))
                output_lines.append('\\end{userprompt}')
                output_lines.append('')
                current_block = []
                in_user_prompt = False
            
            # Start new LLM response
            output_lines.append('\\begin{llmresponse}')
            output_lines.append(sanitize_latex(line))
            in_llm_response = True
            current_block = []
            
        else:
            # Accumulate content for current block
            if in_user_prompt or in_llm_response:
                current_block.append(line)
    
    # Close final block
    if in_user_prompt:
        if current_block:
            content = '\n'.join(current_block).strip()
            if content:
                output_lines.append(content)
        output_lines.append('\\end{userprompt}')
    elif in_llm_response:
        if current_block:
            content = '\n'.join(current_block).strip()
            if content:
                output_lines.append(content)
        output_lines.append('\\end{llmresponse}')
    
    return '\n'.join(output_lines)

def main():
    parser = argparse.ArgumentParser(description='Parse chat logs into LaTeX format')
    parser.add_argument('input_file', help='Input chat log file')
    parser.add_argument('output_file', nargs='?', help='Output LaTeX file (optional)')
    parser.add_argument('--replace-in-tex', help='Replace conversation section in this LaTeX file')
    
    args = parser.parse_args()
    
    try:
        # Read input file
        with open(args.input_file, 'r', encoding='utf-8') as f:
            input_text = f.read()
        
        # Parse the chat logs
        formatted_latex = parse_chat_logs(input_text)
        
        if args.replace_in_tex:
            # Replace conversation section in existing LaTeX file
            with open(args.replace_in_tex, 'r', encoding='utf-8') as f:
                tex_content = f.read()
            
            # Find and replace the conversation log section
            pattern = r'\\subsection\*\{Conversation Log \(formatted\)\}.*?(?=\\end\{document\})'
            replacement = f'\\subsection*{{Conversation Log (formatted)}}\n\n{formatted_latex}\n\n'
            
            new_tex_content = re.sub(pattern, replacement, tex_content, flags=re.DOTALL)
            
            with open(args.replace_in_tex, 'w', encoding='utf-8') as f:
                f.write(new_tex_content)
            
            print(f"✅ Replaced conversation section in {args.replace_in_tex}")
            
        elif args.output_file:
            # Write to output file
            with open(args.output_file, 'w', encoding='utf-8') as f:
                f.write(formatted_latex)
            print(f"✅ Formatted chat logs written to {args.output_file}")
            
        else:
            # Print to stdout
            print(formatted_latex)
            
    except FileNotFoundError:
        print(f"❌ Error: Input file '{args.input_file}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()