#include <bits/stdc++.h>
using namespace std;

 int tab[1006];





int main()
 {
 //freopen("in.txt","r",stdin);
 //freopen("out.txt","w",stdout);
 int t;
  cin>>t;
  for (int w=1;w<t+1;w++)
  {   vector<int>v,aux;
      int n,k;
      memset(tab,0,sizeof tab);
      cin>>n>>k;

      tab[0]=1;
      tab[n+1]=1;
      v.push_back(0);
      v.push_back(n+1);
      int q=(n+1)/2;
      while(k>1)
      {  int s=v.size();

         bool bol=false;
          for (int i=0;i<s-1;i++ )
          {
            if ((v[i+1]-v[i]-1)%2==1)
            {
                if ( tab[(v[i+1]+v[i])/2]==0 && (v[i+1]-v[i]!=1) && (v[i+1]-v[i]!=2)) {
                tab[(v[i+1]+v[i])/2]=1; k--; }
                v.push_back((v[i+1]+v[i])/2);
                 // k--;
                if (k==1) { bol=true;  break;}
            }
            else {
                aux.push_back((v[i+1]+v[i])/2);
            }
          }
          if (bol==false)
          for (int i=0;i<aux.size();i++)
          {
             if (tab[aux[i]]==0) {tab[aux[i]]=1; k--;}
              v.push_back(aux[i]);
              if (k==1) break;
          }
          aux.clear();
          sort(v.begin(),v.end());
          q=(q)/2;

      }
      // for (int i=0;i<v.size();i++) cout<<v[i]<<" ";


    // for (int i=1;i<n+1;i++) cout<<tab[i]<<" ";


      int a=0,c=0;
      for (int i=0;i<n+2;i++)
      {
           if (tab[i]==0) {c++;}
           else {a=max(a,c); c=0; }
      }
      a=max(a,c);



      cout<<"Case #"<<w<<": "<<a/2<<" "<<(a-1)/2<<endl; }

  }

