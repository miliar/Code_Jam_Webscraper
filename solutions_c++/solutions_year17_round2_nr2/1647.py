#include <bits/stdc++.h>
 
#define long long long int
using namespace std;
 
#define Max 100005+5
#define cons 1000000000+7
#define mp make_pair
#define pb push_back
#define x first
#define y second

int main()
{
    ios::sync_with_stdio(false);cin.tie(0);

    freopen("B-small-attempt2.in","r",stdin);
    freopen("output.txt","w",stdout);

    int t;cin>>t;
    int case_No=0;

    while(t--)
    {
    	case_No++;   	
    	cout<<"Case #"<<case_No<<": ";

      // cout<<s.size()<<endl;

      int n;
      cin>>n;

      int r,o,g,y,b,v;cin>>r>>o>>g>>y>>b>>v;
      // cout<<r<<" "<<o<<" "<<y<<" "<<g<<" "<<b<<" "<<v<<"\n";

      if (r>n/2 || g>n/2 || b>n/2)
        {cout<<"Impossible\n";
      continue;}

      vector<pair<int,char> > arr;
      arr.pb({r,'R'});
      arr.pb({g,'Y'});
      arr.pb({b,'B'});

      sort(arr.begin(), arr.end());

      while(arr[2].x>arr[1].x)
      {
        cout<<arr[2].y<<arr[0].y;
        arr[2].x--;
        arr[0].x--;
      }

      while(arr[0].x>0)
      {
        cout<<arr[2].y<<arr[1].y<<arr[0].y;
          arr[2].x--;
          arr[1].x--;
        arr[0].x--;
      

        

      }

      while(arr[2].x>0)
      {
        cout<<arr[2].y<<arr[1].y;
        arr[2].x--;
        arr[1].x--;
      }



          cout<<"\n";
      
    }   	

}





