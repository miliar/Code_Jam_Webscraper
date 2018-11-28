#include <bits/stdc++.h>

using namespace std;

const int maxN = 200005;
const long long inf = 1000000000000000LL;

map< pair< vector<int> , int> , int > mapping;
int P;
int solve(vector<int> mod,int current){

    if(mapping.find({mod , current}) != mapping.end()){
        return mapping[{mod,current}];
    }

    int sum = 0;
    for(int i = 0; i < mod.size(); ++i){
        sum += mod[i];
    }
    if(sum == 0){
        return mapping[{mod,current}] = 0;
    }

    int answer = 0;
    for(int i = 0; i < mod.size(); ++i){
        if(mod[i] > 0){
            mod[i]--;
            answer = max(answer , (current == 0) + solve(mod , (current + i) % P) );
            mod[i]++;
        }
    }
    return mapping[{mod,current}] = answer;
}


int main(){

    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.c","w",stdout);

    int tc , n;
    cin >> tc;

    for(int number_case = 1; number_case <= tc; number_case++){
            scanf("%d %d",&n,&P);

            vector<int> mod(P , 0);
            for(int i = 0; i < n; ++i){
                int x;
                scanf("%d",&x);
                mod[x % P]++;
            }

            mapping.clear();
            printf("Case #%d: %d\n",number_case , solve(mod , 0));
    }


    return 0;
}
