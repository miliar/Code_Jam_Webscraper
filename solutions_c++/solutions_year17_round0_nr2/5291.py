  #include<bits/stdc++.h>     
      using namespace std;  
      typedef long long  ll;
      typedef pair<ll,ll> pll;  
      #define pb(x) push_back(x)     
      typedef unsigned long long  ull;     
      #define mem(A, X) memset(A, X, sizeof A)
      #define ford(i,l,u) for(ll (i)=(ll)(l);(i)>=(ll)(u);--(i))
      #define foreach(e,x) for(__typeof(x.begin()) e=x.begin();e!=x.end();++e)
      #define fori(i,l,u) for(ll (i)=(ll)(l);(i)<=(ll)(u);++(i))    
      typedef pair<int,int> pii;
      #define sec second
      #define fir first  
    
      const ll mod=1e9+7; 
      const ll maxn=1e5+10; 
        
      int main()
      {
           std::ios::sync_with_stdio(false); 
           freopen("in.txt","r",stdin); 
           freopen("out.txt","w",stdout);
           int T;
           while(cin>>T)
           {
            fori(kase,1,T)
            { 
               string s;
               cin>>s;
               if(s.size()>1)
               {
                  int pos=s.size()-2;
                  while(pos>=0)
                  { 
                    if(s[pos]>s[pos+1])
                    {
                        s[pos]--; 
                      fori(i,pos+1,s.size()-1)  s[i]='9'; 
                    } 
                    pos--; 
                  } 

               }
               string ans;
               if(s[0]!='0') ans=s;
               else 
               {
                fori(i,1,s.size()-1) ans+=s[i];
               }
               cout<<"Case #"<<kase<<": "<<ans<<endl;  
            }


           }
        return 0;
      }