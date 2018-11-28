#include <bits/stdc++.h>

using namespace std;
int ingredient[50];
int amount[50][1000001];
int Ihavenow[50];
int DontAplly[50];
vector<pair<int,int> > event[50];

int main()
{
    ifstream cin("B-large (3).in");
    ofstream cout("out.txt");
    int t ;
    cin >> t ;
    for(int tc=1 ; tc<=t ;tc++){

        memset(amount , 0  ,sizeof amount);
        int n , p ;
        cin >> n >> p ;
//        for(int i = ; i<n ; i++)event[i].clear();
        for(int i = 0 ; i<n; i++)cin >> ingredient[i];
        priority_queue< pair<int,pair<int,int> > , vector< pair<int,pair<int,int> > > , greater<pair<int,pair<int,int> > > > Q ;
        for(int i = 0 ; i<n; i++){
            for(int j = 0 ; j< p ; j++){
                int a ;
                cin >> a ;
                int b = a/ingredient[i];
                int l = b ;
                int r = b+1 ;
                double procent = ingredient[i]/10.0;
                while(l>0 &&(double)(a-l*ingredient[i])<= l*procent) l--;
                l++;
                while((double)(r*ingredient[i] - a )<= r*procent)r++;
                if(l!=r){
                    Q.push({l,{1,i}});
                    Q.push({r-1,{2,i}});
                }
            }
        }
        memset(Ihavenow , 0 , sizeof Ihavenow);
        memset(DontAplly , 0 , sizeof DontAplly);
        int ans =0;
        while(!Q.empty()){
            int p = Q.top().first ;
            int a = Q.top().second.first ;
            int in = Q.top().second.second;
////            cout << p << ' ' << a << ' ' << i <<endl;
            Q.pop();
            if(a==1){
                Ihavenow[in]++;
                int tot = 0 ;
                for(int i = 0 ; i<n ; i++){
                    tot+=(Ihavenow[i]>0);
                }
                if(tot==n){
                    ans++;
                    for(int i = 0 ; i<n ; i++){
                        DontAplly[i]++;
                        Ihavenow[i]--;
                    }
                }
            }
            else{
                if(DontAplly[in])DontAplly[in]--;
                else Ihavenow[in]--;
            }
        }

        cout << "Case #" << tc << ": "<< ans<< "\n";
    }
    return 0;
}
