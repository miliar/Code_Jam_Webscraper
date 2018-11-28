#include <fstream>

using namespace std;

ifstream cin("date.in");
ofstream cout("date.out");

int TMAX;
int v[10000];
int nr;

bool isTidy(){
    int cifMin = v[0];
    for(int i = 1; i < nr; i++){
        if(v[i] < cifMin){
            return 0;
        }else{
            cifMin = v[i];
        }
    }
    return 1;
}

int main(){
    cin >> TMAX;

    for(int t = 1; t <= TMAX; t++){
        unsigned long long x;
        cin >> x;
        unsigned long long aux = x;
        nr = 0;
        while(aux != 0){
            aux /= 10;
            nr++;
        }
        for(int i = nr-1; i >= 0; i--){
            v[i] = x%10;
            x /= 10;
        }

        for(int i = 0; i < nr; i++){
            //cout << v[i];
        }

        int lst = nr -1;
        while(!isTidy()){
            while(lst > 0 && v[lst] == 0){
                v[lst] = 9;
                lst--;
            }
            v[lst]--;
        }
        cout << "Case #" << t << ": ";
        int i = 0;
        while(v[i] == 0){
            i++;
        }
        for(;i < nr; i++){
            cout << v[i];
        }
        cout << '\n';
    }

    return 0;
}
