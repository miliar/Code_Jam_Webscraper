#include<bits/stdc++.h>
using namespace std;
long long int arr[50];
int main()
{
    long long int t;
    cin>>t;
    long long int n;
    for(long long int p=1;p<=t;p++)
    {
        cin>>n;
        map<long long int,long long int> m;
        m[n]=1;
        long long int k;cin>>k;
        vector<long long int> vec;
        set<long long int> s;
        s.insert(-1*n);
        long long int j=0;
        long long int l=0;
        set<long long int>::iterator it = s.begin();
        long long int ch = *it;
        ch=-1*ch;
        while(j+m[ch]<k)
        {


            if(ch%2!=0)
            {
                m[ch/2]+=2*m[ch];
                s.insert(-1*(ch/2));
            }
            else
            {
                m[ch/2]+=m[ch];
                m[ch/2-1]+=m[ch];
                s.insert(-1*(ch/2));
                s.insert(-1*(ch/2-1));
            }
           // cout<<ch<<endl;
            it++;
            j+=m[ch];
            ch = *it;
            ch=-1*ch;

        }
        l = *it;
        l=-1*l;
        if(l%2==0)
        {
            cout<<"Case #"<<p<<": "<<l/2<<' '<<l/2-1<<endl;
        }
        else cout<<"Case #"<<p<<": "<<l/2<<' '<<l/2<<endl;
    }
}
