#include <vector>
#include <iostream>
#include <map>
#include <tuple>
using namespace std;


struct task {
    int beg;
    int end;

};


bool between(int a, int b, int c, int d){

    if(c < d){
        if (a >= c and a <= d){
            if(b >= c and b <= d){
                return true;
            }
        }
        return false;
    }
    else {
        if(a <= d and b <= d){
            return true;
        }
        if(a >= c and b >= c){
            return true;
        }
    }
    return false;
}
int main(){
    int n;
    cin >> n;
    for(int i = 0; i < n; i++){

    

        int ci, di;
        cin >> ci >> di;

        vector<task> tc;
        vector<task> td;

        for(int j = 0; j < ci; j ++){
       
          task tmp;
          cin >> tmp.beg;
          cin >> tmp.end;

          tc.push_back(tmp); 
        }
        for(int j = 0; j < di; j ++){
       
          task tmp;
          cin >> tmp.beg;
          cin >> tmp.end;

          td.push_back(tmp); 
        }



        bool solved = false;
        for(int i = 0; i < 2 * 720 ;i ++){
            solved = true;
            int end = (i + 720) % 1440; 
            for(auto a : td){
                if(!between(a.beg, a.end, i, end)){
                    solved = false; 
                }
            }
            for(auto a : tc){
                if(!between(a.beg, a.end, end, i)){
                    solved = false; 
                }

            }
            if (solved){
                break;
            }
        }
        cout << "Case #" << i + 1<< ": ";
        if(solved){
            cout << 2;
        } else {
            cout << 4;
        }

        cout << endl;

    }
}
