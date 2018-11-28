#include <iostream>
#include<fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <math.h>
using namespace std;

int main()
{

    FILE *fin = freopen("C:/Users/trigfan/Desktop/GoogleCodeJam/Round1/1B/B-large.in", "r", stdin);
	FILE *fout = freopen("C:/Users/trigfan/Desktop/GoogleCodeJam/Round1/1B/B-large.out", "w", stdout);
    int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
        int N,P,ans=0;
        long c,l,r,d;
        long x;
        cin>>N>>P;
        vector<long> M;
        vector<long> V[N];
        for(int i=0; i<N; i++)
        {
            cin>>x;
            M.push_back(x);
        }
        for(int i=0; i<N; i++)
        {
            for(int j=0; j<P; j++)
            {
                cin>>x;
                V[i].push_back(x);

            }
            sort(V[i].begin(),V[i].end());

        }


        c=P;
        bool y=true;
        while(y)
        {
            l=0;
            r=10000000;
            bool check=true;
            for(int i=0; i<N; i++)
            {
                if(!V[i].empty())
                {
                    long double a,b;

                    a=((double(V[i].back())/M[i])/1.1);
                    b=((double(V[i].back())/M[i])/0.9);

                    if(l<ceil(a))
                    {
                        l=ceil(a);
                        d=i;
                    }

                    if(floor(b)<r)
                        r=floor(b);

                    if(r<l)
                    {
                        check=false;
                        V[d].pop_back();
                        break;
                    }
                }
                else
                {
                    y=false;
                    check=false;
                    break;
                }
            }


            if(check)
            {
                for(int i=0; i<N; i++)
                    V[i].pop_back();
                ans++;
            }


        }


        cout << "Case #" << t << ": ";
        cout<<ans<<endl;
	}
    return 0;
}
