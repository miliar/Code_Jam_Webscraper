#include<bits/stdc++.h>

using namespace std;

int main()
{
    ofstream cout; ifstream cin;
    cout.open("out_large.txt");
    cin.open("large.in");
    unsigned long long t,T,n,i,k,ele;
    cin>>T;
    set< unsigned long long> s;
    map< unsigned long long, unsigned long long> m;
    for(t=1;t<=T;t++)
    {
        s.clear(); m.clear();
        cin>>n;
        cin>>k;
        s.insert(n);
        m[n]=1;
        i=0;
        while(i<k)
        {
            ele=*(s.rbegin());
            s.erase(ele);
            i+=(m[ele]);
            ele--;
            s.insert(ele/2);
            if(m.find(ele/2)!=m.end()){m[ele/2]+=(m[ele+1]);}
            else{m[ele/2]=m[ele+1];}
            s.insert((ele+1)/2);
            if(m.find((ele+1)/2)!=m.end()){m[(ele+1)/2]+=(m[ele+1]);}
            else{m[(ele+1)/2]=m[ele+1];}
            m[ele+1]=0;
        }
        cout<<"Case #"<<t<<": "<<(ele+1)/2<<" "<<ele/2<<"\n";
    }
    return 0;
}
