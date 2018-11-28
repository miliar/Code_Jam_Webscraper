#include <bits/stdc++.h>

using namespace std;

void Solve(int numbercase){

    int n , k;
    cin >> n >> k;
    n+=2;

    vector<bool> ocuppied(n, false);
    ocuppied[0] = true;
    ocuppied[n - 1] = true;

    int who;
    vector< pair<int,int> > information(n);
    while( k > 0){

        int last = 0;
        for(int i = 1; i < n - 1; ++i){
            if(ocuppied[i] == true){
                last = i;
            }else{
                information[i].first = i - last - 1;
            }
        }
        last = n - 1;
        for(int i = n - 2; i >= 1; i--){
                if(ocuppied[i] == true){
                    last = i;
                }else{
                    information[i].second = last - i - 1;
                }
        }

        who = -1;
        for(int i = 1; i < n - 1; ++i){
            if(ocuppied[i]){
                continue;
            }
            if(who == -1 || min(information[i].first,information[i].second) > min(information[who].first , information[who].second)
               || (min(information[i].first,information[i].second) == min(information[who].first , information[who].second) &&
                   max(information[i].first,information[i].second) > max(information[who].first , information[who].second) ) ){
                    who = i;
            }
        }
        ocuppied[who] = true;
        k--;
    }
    if(information[who].first < information[who].second){
        swap(information[who].first, information[who].second);
    }
    printf("Case #%d: %d %d\n",numbercase , information[who].first,information[who].second);

}


int main(){

    freopen("C-small-1-attempt0.in","r",stdin);
    freopen("output.c","w",stdout);

    int tc;
    cin >> tc;
    for(int numbercase = 1; numbercase <= tc; numbercase++){
        Solve(numbercase);
    }



    return 0;
}
