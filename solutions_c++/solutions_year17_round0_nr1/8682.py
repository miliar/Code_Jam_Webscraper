 #include <bits/stdc++.h>
using namespace std;

int n, k, sz;
string in;

void Try(bool &bad, int &cnt)
{
    string x=in;
    for(int i=0;i<sz;i++){
         if(i+k>sz){
            if(x[i]=='-'){
                bad=true;
                break;
            }
         }
         else if(x[i]=='-'){
            cnt++;
            for(int j=i+1;j<i+k;j++){
                if(x[j]=='-')
                    x[j]='+';
                else
                    x[j]='-';
            }
         }
       }
}

int main()
{
   freopen("r.txt","r",stdin);
   freopen("out.txt","w",stdout);
   cin>>n;
   for(int i=0;i<n;i++){
       bool bad1=false, bad2=false, bad=true;
       int cnt1=0, cnt2=0, cnt=0;
       cin>>in>>k;
       sz=in.size();

       Try(bad1, cnt1);
       reverse(in.begin(), in.end());
       Try(bad2, cnt2);

       if(bad1==false || bad2==false)
            bad=false;
       if(bad1==false && bad2==false)
            cnt=min(cnt1, cnt2);
       if(bad1==false && bad2==true)
            cnt=cnt1;
       if(bad1==true && bad2==false)
            cnt=cnt2;

       cout<<"Case #"<<i+1<<": ";
       if(bad)
        cout<<"IMPOSSIBLE\n";
       else
        cout<<cnt<<"\n";
   }
    return 0;
}
