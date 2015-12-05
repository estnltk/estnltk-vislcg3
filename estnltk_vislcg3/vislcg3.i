%module vislcg3


%{
// wrap the vislcg3 binary main method
int vislcg3_main(int argc, char *argv[]);
%}

int vislcg3_main(int, char **);

