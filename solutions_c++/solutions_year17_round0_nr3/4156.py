#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t,n=0,k=0,x=0;
    int num;
    fstream fin,fout;
    int  max, min;

    fin.open("C-small-2-attempt0.in",ios::in);
    fout.open("Output.txt",ios::out);

    fin>>t;

    for(int x=1; x<=t; x++)
    {
        fin>>n;
        fin>>k;

        priority_queue<long int> q;
        q.push(n);
        for(int i=0; i<k; i++)
        {
            num = q.top();
            q.pop();
            max = num/2;
            min = num - num/2 - 1;

            q.push(min);
            q.push(max);
         }
        fout<<"Case #"<<x<<": "<<max<<" "<<min<<"\n";
    }

    fout.close();
    fin.close();
    return 0;
}

