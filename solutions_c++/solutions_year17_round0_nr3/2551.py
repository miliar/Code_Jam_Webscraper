#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    ifstream in; in.open("C-large.in");
    ofstream out; out.open("out.txt");

    int T; in >> T;

    long long N,K,val;

    for(int x = 1 ; x <= T ; x++)
    {
        in >> N >> K;
        out << "Case #" << x << ": ";

        map <long long,long long> mp;
        mp[-N]=1;
        map<long long,long long>::iterator it = mp.begin();
        for( ; it!=mp.end() ; it++)
        {
            val= -(it->first);
            if(val%2==0)
            {
                if(val>1) mp[-(val/2)]+=(it->second);
                if(val>2) mp[-(val/2-1)]+=(it->second);
            }
            else
            {
                if(val>1) mp[-(val/2)]+=2*(it->second);
            }
        }

        it = mp.begin();
        for( ; it!=mp.end() ; it++)
        {
            K-=(it->second);
            if(K<=0)
            {
                val=-(it->first);

                if(val%2==0) out << val/2 << ' ' << val/2-1 << "\n";
                else out << val/2 << ' ' << val/2 << "\n";

                break;
            }
        }
    }
    return 0;
}
