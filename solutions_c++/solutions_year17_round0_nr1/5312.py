//* ____________________
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
          int k;
          cin>>s>>k; 


          bitset<1000+10> bs;
          fori(i,0,s.size()-1)  
          {
            if(s[i]=='+') bs[i]=0;  // 0 +
            else bs[i]=1;
          }

          int cnt=0;  

          int cur=0;
          while(cur<=(int)s.size()-1-k+1)
            {
              if(bs[cur]) 
              {
                fori(i,cur,cur+k-1) bs[i]=!bs[i];
                cnt++; 
              } 
               cur++;
            }
            fori(pos,cur,s.size()-1) { if(bs[pos]==1) cnt=-1; }
 
          if(cnt==-1) cout<<"Case #"<<kase<<": IMPOSSIBLE"<<endl;
          else cout<<"Case #"<<kase<<": "<<cnt<<endl;
        }

       }
    return 0;
  }