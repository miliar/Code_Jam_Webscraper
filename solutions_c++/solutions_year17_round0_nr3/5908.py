#include<bits/stdc++.h>
using namespace std;
int main()
{
    int test;
    cin >> test;
    for (int i = 1; i <= test; ++i)
    {
        vector<long long> vect;
        long long int n,k,ans1,ans2;
        cin>>n>>k;

        vect.push_back(n);
        while(k--)
        {
            sort (vect.begin(),vect.end(),greater<long long >());
            long long temp=vect[0];
            vect.erase (vect.begin());
            if(temp%2==0)
            {
                vect.push_back(temp/2);
                vect.push_back(temp/2-1);
                ans1=temp/2;
                ans2=temp/2-1;
            }
            else
            {
                vect.push_back(temp/2);
                vect.push_back(temp/2);
                ans1=temp/2;
                ans2=temp/2;
            }
        }
        sort (vect.begin(),vect.end(),greater<long long >());
        long l=vect.size();
        cout << "Case #" << i << ": " << ans1<<" "<<ans2<< endl;
    }
}
