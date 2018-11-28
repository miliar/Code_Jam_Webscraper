#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <string.h>
#include <algorithm>

typedef long long int LL;

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
        int r, c;
        fscanf(in, "%d %d", &r, &c);
		vector<vector <char> > cake(r, vector<char>(c));
		for(int i=0; i<r; ++i)
		{
		    char readin[100];
			fscanf(in, "%s", readin);
			for(int j=0; j<c; ++j)
            {
                cake[i][j]=readin[j];
            }
		}
        for(int i=0; i<r; ++i)
		{
		    char lastValid = '0';
			for(int j=0; j<c; ++j)
            {
                char was = cake[i][j];
                if(cake[i][j]=='?' && lastValid!='0')
                {
                    cake[i][j]=lastValid;
                }
                else if(cake[i][j]!='?' && lastValid=='0')
                {
                    for(int k=j-1; k>=0; --k)
                    {
                        cake[i][k]=cake[i][j];
                    }
                }
                if(was!='?')
                    lastValid = was;
            }
		}

        for(int i=0; i<r; ++i)
		{
		    if(cake[i][0]!='?')
                continue;

            if(i>0 && cake[i-1][0]!='?')
            {
                for(int j=0; j<c; ++j)
                {
                    cake[i][j]=cake[i-1][j];
                }
            }
		}
		for(int i=r-1; i>=0; --i)
		{
		    if(cake[i][0]!='?')
                continue;

            if(i<r-1 && cake[i+1][0]!='?')
            {
                for(int j=0; j<c; ++j)
                {
                    cake[i][j]=cake[i+1][j];
                }
            }
		}


        fprintf(out, "Case #%d: \n", t+1);
        for(int i=0; i<r; ++i)
		{
			for(int j=0; j<c; ++j)
            {
                fprintf(out, "%c", cake[i][j]);
            }
            fprintf(out, "\n");
		}
    }

    fclose(in);
    fclose(out);
    return 0;
}
