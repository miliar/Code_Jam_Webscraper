  // #include<bits/stdc++.h>     
  //     using namespace std;  
  //     typedef long long  ll;
  //     typedef pair<ll,ll> pll;  
  //     #define pb(x) push_back(x)     
  //     typedef unsigned long long  ull;     
  //     #define mem(A, X) memset(A, X, sizeof A)
  //     #define ford(i,l,u) for(ll (i)=(ll)(l);(i)>=(ll)(u);--(i))
  //     #define foreach(e,x) for(__typeof(x.begin()) e=x.begin();e!=x.end();++e)
  //     #define fori(i,l,u) for(ll (i)=(ll)(l);(i)<=(ll)(u);++(i))    
  //     typedef pair<int,int> pii;
  //     #define sec second
  //     #define fir first  
    
  //     const ll mod=1e9+7; 
  //     const ll maxn=1e5+10; 
        
  //     int main()
  //     {
  //          std::ios::sync_with_stdio(false); 
  //          freopen("in.txt","r",stdin); 
  //          freopen("out.txt","w",stdout);
  //          int T;
  //          while(cin>>T)
  //          {
  //           fori(kase,1,T)
  //           { 
  //              string s;
  //              cin>>s;
  //              if(s.size()>1)
  //              {
  //                 int pos=s.size()-2;
  //                 while(pos>=0)
  //                 { 
  //                   if(s[pos]>s[pos+1])
  //                   {
  //                       s[pos]--; 
  //                     fori(i,pos+1,s.size()-1)  s[i]='9'; 
  //                   } 
  //                   pos--; 
  //                 } 

  //              }
  //              string ans;
  //              if(s[0]!='0') ans=s;
  //              else 
  //              {
  //               fori(i,1,s.size()-1) ans+=s[i];
  //              }
  //              cout<<"Case #"<<kase<<": "<<ans<<endl;  
  //           }


  //          }
  //       return 0;
  //     }

  
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
  const ll INF=0xffffffff;
  const ll mod=1e9+7; 
  const ll maxn=1e5+10; 
   ll n,k;
  const ll maxk=1e3+10;
  

  struct node
  {
    int ls,ms,id;
    bool  have_occupied;
  }  ele[maxk];
  void init()
  {
    //init the ele .
    fori(pos,1,n)
    {
      ele[pos].id=pos;
      ele[pos].ls=pos-1;
      ele[pos].ms=n-pos;
      ele[pos].have_occupied=false;
    }


  } 

  vector<int>  get_best_le()
  {
    // according to current ele info 

    int max_ls=-1;
    fori(i,1,n) { if(ele[i].have_occupied==true) continue; int temp_ls=ele[i].ls; max_ls=max(max_ls,min(temp_ls,ele[i].ms) );  }

    vector<int> all_best_le_id;
    fori(i,1,n) { if(ele[i].have_occupied==true) continue;   int temp_ls=ele[i].ls; if(min(temp_ls,ele[i].ms)==max_ls ) all_best_le_id.push_back(ele[i].id);}

    return all_best_le_id;
  }

  vector<int> get_best_ms(vector<int> all_best_ls_id)
  {
    //get best according to the right 

    int max_ms=-1;
    fori(i,0,(int)all_best_ls_id.size()-1)
    {
      int temp_id=all_best_ls_id[i];
      int temp_ms=ele[temp_id].ms;
      max_ms=max(max_ms,max(ele[temp_id].ls,temp_ms) );
    }
    
    vector<int> all_best_ms;
    fori(i,0,(int)all_best_ls_id.size()-1)
    {
      int temp_id=all_best_ls_id[i];
      int temp_ms=ele[temp_id].ms;
      if(max(temp_ms,ele[temp_id].ls)==max_ms)  all_best_ms.push_back(temp_id); 

    }
    return all_best_ms; 
  }

  int get_best_left(vector<int> all_best_ms)
  {
    ll final_pos=INF;

    fori(i,0,(int)all_best_ms.size()-1)
    {
      int temp_id=all_best_ms[i];
      final_pos=min(final_pos,(ll)temp_id);
    }

    return final_pos;

  }
  int get_best_pos()
  {
    vector<int> all_best_ls_id=get_best_le();

    vector<int> best_ms=get_best_ms(all_best_ls_id);

    int best_pos_id=get_best_left(best_ms);
    //cout<<best_pos_id<<endl;
    return best_pos_id;

  }
  void update_related(int the_pos_id)
  {
    //cout<<"the_pos: "<<the_pos_id<<endl;
     ele[the_pos_id].have_occupied=true;  
     // only need to update the adjected that not been occupied

     int to_right=the_pos_id;
     while(++to_right<=n&&ele[to_right].have_occupied==false)
     {
        ele[to_right].ls=to_right-the_pos_id-1; 
     }

     int to_left=the_pos_id;
     while(--to_left>=1&&ele[to_left].have_occupied==false)
     {
      ele[to_left].ms=the_pos_id-to_left-1;
     } 

  }
  int klx,kmx;
  void get_ans(int id)
  {
    //cout<<"id: "<<id<<endl;
    int a=ele[id].ls;
    int b=ele[id].ms; 
    klx=max(a,b);
    kmx=min(a,b);
  }

  void solve()
  {
    //by analog

    init();

    fori(i,1,k)
    {
      int the_pos_id=get_best_pos();  
      update_related(the_pos_id); 

      if(i==k)  get_ans(the_pos_id); 

    } 

  }


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
          cin>>n>>k; 
          solve();
          cout<<"Case #"<<kase<<": "<<klx<<" "<<kmx<<endl;
        } 

       }
    return 0;
  }

 /*__________
    analysis:
    debug   : 
    note    :   
  */ 
