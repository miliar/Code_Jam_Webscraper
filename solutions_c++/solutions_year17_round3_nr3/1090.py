#include<bits/stdc++.h>
using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;

    fin.open("input.in", ios::in);
    fout.open("output2.txt", ios::out);

    int t;
    fin>>t;
    int cas = 0;
    while(t--)
    {
        cas++;
        int n, k;
        fin>>n>>k;

        double che;
        fin>>che;

        double arr[n];
        for(int i=0; i<n; i++)
            fin>>arr[i];

        if(n == k)
        {
            while(che > 0)
            {
                sort(&arr[0], &arr[n]);
                int ctr = 1;
                int j = 1;
                while(arr[j]==arr[j-1] && j<n)
                {
                    ctr++;
                    j++;
                }

                if(j<n)
                {
                    double diff = arr[j] - arr[j-1];
                    double nakhvapadse = diff*ctr;

                    if(che >= nakhvapadse)
                    {
                        double toadd = diff;
                        che -= nakhvapadse;
                        for(int i=0; i<ctr; i++)
                            arr[i] += toadd;
                    }
                    else
                    {
                        double toadd = che/ctr;
                        che = 0;
                        for(int i=0; i<ctr; i++)
                            arr[i] += toadd;
                    }
                }
                else
                {
                    double toadd = che/ctr;
                    for(int i=0; i<n; i++)
                        arr[i] += toadd;
                    che = 0;
                }
            }
        }

        double ans = 1;
        for(int i=0; i<n; i++)
            ans *= arr[i];
        fout<<"Case #"<<cas<<": "<<std::fixed<<std::setprecision(6)<<ans<<endl;
    }

    fin.close();
    fout.close();
}
