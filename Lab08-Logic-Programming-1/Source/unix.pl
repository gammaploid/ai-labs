% Student Name: Hassan Almosa
% Student FAN: Alia0024
% File: unix.pl
% Date: 10-11-2025
% Description: A Prolog knowledge base representing a simple UNIX-like file system.

% root dir 

location(bin, root).
location(etc, root).
location(sbin, root).
location(usr, root).
location(var, root).
location(home, root).
location(lib, root).
location(tmp, root).
location(dev, root).
location(proc, root).
location(opt, root).
location(mnt, root).

% /bin dir
location(bash, bin).
location(cat, bin).
location(ls, bin).
location(cp, bin).
location(mv, bin).
location(rm, bin).


% /etc dir
location(crontab, etc).
location(cups, etc).
location(fonts, etc).
location(fstab, etc).
location('host.conf', etc).
location(bash, etc).


% /usr dir
location(bin, usr).
location(include, usr).
location(lib, usr).
location(local, usr).

% /usr/local dir
location(bin, local).
location(lib, local).
location(man, local).
location(share, local).

%%%%%%%
% FACTS
%%%%%%%%

% facts about folders
folder(root).
folder(local).
folder(usr).
folder(etc).
folder(bin).
folder(var).
folder(home).
folder(sbin).
folder(lib).
folder(tmp).
folder(dev).
folder(proc).
folder(opt).
folder(mnt).    

% facts about files
file(crontab).
file(cups).
file(fonts).
file(fstab).
file('host.conf').
file(bash).



%%%%%%%%
% RULES
%%%%%%%%

is_in_grandparent(Item, GrandparentFolder) :- location(Item, Parent), location(Parent, GrandparentFolder).

find_path(Item, [root]) :-           % Base case: path is [root]
    location(Item, root).

find_path(Item, Path) :- 
    location(Item, Parent),
    Parent \= root,
    find_path(Parent, ParentPath),
    append(ParentPath, [Parent], Path).  % Append [Parent] to build path