#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <vector>
#include <list>
#include <string.h>
#include <map>

using namespace std;

int main()
{
    FILE* in, *out;
    string filename = "B-large";
    string infilename = filename, outfilename = filename;
    infilename+=".in";
    outfilename+=".out";
    if((in=fopen(infilename.c_str(), "rt"))==NULL)
    {
        cout<<"Input file not found."<<endl;
        getchar();
        return 1;
    }
    if((out=fopen(outfilename.c_str(), "wt"))==NULL)
    {
        cout<<"Cannot create output file."<<endl;
        getchar();
        return 2;
    }

    int T;
    fscanf(in, "%d", &T);

    for(int t=0; t!=T; ++t)
    {
        char s[100];
        fscanf(in, "%s", s);

        int sz=strlen(s);
        if(sz<2)
        {
            fprintf(out, "Case #%d: %s\n", t+1, s);
            continue;
        }
        for(int i=sz-2; i>=0; --i)
        {
            if(s[i]>s[i+1])
            {
                --s[i];
                for(int j=i+1; j<sz; ++j)
                {
                    s[j]='9';
                }
            }
        }

        fprintf(out, "Case #%d: ", t+1);
        int i;
        for(i=0; i<sz; ++i)
        {
            if(s[i]>'0')
                break;
        }
        for(; i<sz; ++i)
        {
            fprintf(out, "%c", s[i]);
        }
        fprintf(out, "\n");

    }

    fclose(in);
    fclose(out);
    return 0;
}
