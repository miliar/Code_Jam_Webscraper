#include <bits/stdc++.h>
using namespace std;
long long getno(string s)
{
    long long ans=0;
    long long f=1;
    for(long i=s.length()-1;i>=0;i--){
        ans+= (s[i]-'0')*f;
        f=f*10;
    }
    return ans;
}
int main()
{
    //freopen("test1.txt","r",stdin);
    //freopen("file1.txt","w",stdout);
    long long t,n;
    string s;
    cin>>t;
    long cnt=0;
    while(t--)
    {
        cnt++;
        cout<<"Case #"<<cnt<<": ";
        cin>>s;
        /*n=getno(s);
        vector<long long > v;
        long long ans1=0;
        for(long long i=n;i>=1;i--){
            long long j= i;
            v.clear();
            while(j){
                long long p= j%10;
                v.push_back(p);
                j/=10;
            }
            int flagger=0;
            for(long long j=v.size()-1;j>=1;j--){
                if(v[j]> v[j-1]){
                    flagger=1;
                    break;
                }
            }
            if(flagger==0){
                ans1=i;
                break;
            }
        }*/
        long flag=0;
        long abs=0;
        for(long long l=1;l<=18;l++){
        long long mark=s.length();
        flag=0;
        for(long i=0;i<s.length()-1;i++){
            long b = s[i+1]-'0';
            long a= s[i]-'0';
            if(a>b){
                abs=1;
                flag=1;
                s[i]--;
                mark=i+1;
                break;
            }
        }
        for(long i=mark;i<s.length();i++){
            s[i]='9';
        }
        if(flag==0)
            break;
        }
        //cout<<s<<endl;
        //cout<<ans1<<" ";
        if(abs==0)
            cout<<s<<endl;
        else{
            long long st=0;
            for(long long i=0;i<s.length();i++){
                if(s[i]!='0'){
                    st=i;
                    break;
                }
            }
            for(long i=st;i<s.length();i++){
                cout<<s[i];
            }
            cout<<endl;
        }
        //long long n2= getno(s);
        //if(ans1 != n2)
            //cout<<"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"<<endl;
    }
}

