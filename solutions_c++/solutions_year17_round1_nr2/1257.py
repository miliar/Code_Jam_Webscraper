#include<bits/stdc++.h>
#define LL long long
using namespace std;


int minValid(int x,int y){
    int want = y;
    while( want<=int(x/0.9) ){
        if( int(want*0.9)<=x && int(want*1.1)>=x ){
            return want/y;
        }
        want+=y;
        //cout<<"\nwant :"<<want;
    }
    return -1;
}


int maxValid(int x,int y){
     int want = y;
     bool flag=false;
    while( want<=int(x/0.9) ){
        while( int(want*0.9)<=x && int(want*1.1)>=x ){
            flag=true;
            want+=y;
        }
        if(flag==false)
            want+=y;
    }

    if(flag==false)
    return -1;
        else
    return want/y - 1;


}





int main()
{
  int t, n, m , p , x;
  cin >> t;
  for (int k = 1; k <= t; ++k)
  {
    vector<int>  P[52];
    int want[52];
    int index[52];
    int Tmax[52];
    LL ans=0;

    cin >> n >> p;

    for(int i=0; i<n; i++)cin>>want[i];

    for(int i=0; i<n; i++){
        for(int j=0; j<p; j++){
            cin>>x;
            P[i].push_back(x);
        }
    }

    for(int i=0; i<n; i++)
        sort(P[i].begin(),P[i].end());

    for(int i=0; i<n; i++)index[i]=0;

    bool flag = true ;
    while(flag)
    {
        int mini , maxi ;
        mini =  (int)( minValid( P[0][ index[0] ],want[0]) )  ;
        maxi =  (int)( maxValid( P[0][ index[0] ],want[0]) ) ;
        Tmax[0]=maxi;

        //cout<<mini<<"  "<<maxi<<endl;
        for(int i=1; i<n; i++)
        {
            Tmax[i] =  (int)( maxValid( P[i][ index[i] ],want[i]) );

            mini =  max( mini , (int)( minValid( P[i][ index[i] ],want[i]) ) );
            maxi =  min( maxi , (int)( maxValid( P[i][ index[i] ],want[i]) ) );
        }
        //cout<<"ok\n";

        if(mini<=maxi && mini!=-1 ){
            ans++;
            for(int i=0; i<n; i++){
                index[i]++;
                if(index[i]==p)flag=false;
            }
        }else{
            int t_maxi = Tmax[0] , t_index = 0 ;
            for(int i=1; i<n; i++){
                if(Tmax[i]<t_maxi){
                    t_maxi = Tmax[i];
                    t_index=i;
                }
            }
            index[t_index]++;
            if(index[t_index]==p)flag=false;
        }
    }
    cout << "Case #" << k << ": " << ans << endl;
  }
  return 0;
}
