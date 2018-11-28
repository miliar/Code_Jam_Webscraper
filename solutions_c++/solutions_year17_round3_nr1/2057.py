#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(), (x).end()
#define len(x) (int)(x).size()
#define PI acos(-1)
#define xx first
#define yy second
#define max(x,y) x > y ? x:y
using namespace std;

int T,N, K;

int main(){
    cin >> T;
    for(int t =1;t <= T;t++){
        cin >> N >> K;
        vector< pair<int,int> >pancakes;
        for(int i = 0;i < N;i++){
            int r,h;
            cin >> r >> h;
            pancakes.pb(mp(r,h));
        }
        sort(all(pancakes));
        double ans = 0;
        do{
            bool pos = true;
            for(int i = 1;i < K;i++){
                if(pancakes[i].xx > pancakes[i-1].xx){
                    pos = false;
                }
            }
            if(!pos){
                continue;
            }
            double area = 0;
            for(int i = 0;i < K;i++){
                area += PI*pancakes[i].xx*pancakes[i].xx 
                        + 2*PI*pancakes[i].xx*pancakes[i].yy;
                if(i > 0){
                    area -= PI*pancakes[i].xx*pancakes[i].xx; 
                }
            }
            ans = max(ans, area);
        }while(next_permutation(all(pancakes)));
        printf("Case #%d: %.9lf\n", t, ans);
    }
    return 0;
}
