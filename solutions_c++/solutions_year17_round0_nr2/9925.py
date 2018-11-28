  #include<bits/stdc++.h>
  using namespace std;

  bool check(long long n)
  {
    vector<int> v;
    long long i,t=n;
    while(t!=0)
    {
      v.push_back(t%10);
      t/=10;
    }
    int f=0;
    for( i=(int)v.size()-2;i>=0;i--)
    {
      if(v[i]<v[i+1])break;
    }
    if(i==-1)return 1;
    else return 0;
  }
  int main()
  {
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for(int j=1;j<=t;j++)
    {long long n;
    cin>>n;
    while(!check(n))
    {
      vector<int> v;
      long long t=n;
      while(t!=0)
      {
        v.push_back(t%10);
        t/=10;
      }
      int f=0;
      for(int i=(int)v.size()-2;i>=0;i--)
      {
        if(f==1)v[i]=9;
        else if(v[i]<v[i+1]){v[i]=9,v[i+1]-=1;f=1;}
      }

      long long po=1;
      n=0;
      for(int i=0;i<v.size();i++)
      {
        n+=po*v[i];
        po*=10LL;
      }
    }
    cout<<"Case #"<<j<<": ";
    cout<<n<<endl;

  }
    return 0;
  }
