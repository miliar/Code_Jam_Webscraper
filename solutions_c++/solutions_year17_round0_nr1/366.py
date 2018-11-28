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
    string filename = "A-large";
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
        int k;
        char s[3000];
        fscanf(in, "%s %d", s, &k);

        int sz=strlen(s);
        vector<int> p(sz);
        for(int i=0; i<sz; ++i)
        {
            if(s[i]=='+')
                p[i]=0;
            else if(s[i]=='-')
                p[i]=1;
            else
                cout<<"FORMAT ERROR"<<endl;
        }

        int flips = 0;
        int i;
        for(i=0; i<=sz-k; ++i)
        {
            if(p[i]==1)
            {
                ++flips;
                for(int j=0; j<k; ++j)
                {
                    p[i+j]=(p[i+j]+1)%2;
                }
            }
        }
        bool impo=false;
        for(; i<sz; ++i)
        {
            if(p[i]==1)
                impo=true;
        }

        if(impo)
            fprintf(out, "Case #%d: IMPOSSIBLE\n", t+1);
        else
            fprintf(out, "Case #%d: %d\n", t+1, flips);
    }

    fclose(in);
    fclose(out);
    return 0;
}
