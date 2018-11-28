#include <iostream>
#include <map>
#include <utility>

using namespace std;

int N, K, T;
map<int, int> m;

int main(){


    cin >> T;
    for(int t = 1; t <= T; t++){
        cin >> N >> K;
        int i = 1;
        m.clear();
        m.insert(make_pair(N, 1));
        int answer1 = -1;
        int answer2 = -1;
        while(i <= K){

            int act = m.rbegin()->first;
            int num = m.rbegin()->second;;
            if(num > 1){
                m.find(act)->second = num-1;
            }else{
                m.erase(act);
            }

            int x = -1;
            int y = -1;
            if(act%2==1){
                x = act/2;
                y = act/2;
            }else{
                x = act/2-1;
                y = act/2;
            }

            if(m.find(x) == m.end()){
                m.insert(make_pair(x, 1));
            }else{
                m.find(x)->second = m.find(x)->second+1;
            }
            if(m.find(y) == m.end()){
                m.insert(make_pair(y, 1));
            }else{
                m.find(y)->second = m.find(y)->second+1;
            }


            if(i == K){
                answer1 = y;
                answer2 = x;
            }


            //cout << "iteration " << i << " act " << act << " num " << num << " x " << x << " y " << y << endl;



            i++;
        }
        cout << "Case #" << t << ": " << answer1 << " " << answer2 << endl;


    }






    return 0;
}
