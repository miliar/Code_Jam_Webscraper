
#include <vector>
#include <iostream>
using namespace std;

vector<char> lastrow;

int count(vector<char> & in){
    int ret = 0;
    for(auto a : in ){
        if(a != '?'){
            ret++;
        }
    }
    return ret;
}


void filrow(vector<char> & in){
    if(0 != count(in)){
        int last = 0;
        char lastchar = ' ';
        for(int i = 0; i < in.size(); i ++){
            if(in[i] != '?'){
                lastchar = in[i];
                for(int j = last; j < i; j ++){
                    in[j] = in[i];
                } 
                last = i + 1;
            }
        }
        for(int i = last; i < in.size(); i ++){
            in[i] = lastchar;
        }
        lastrow = in;
    }
    else {
        in = lastrow;
    }

}



int main(){
    int n;
    cin >> n;
    for(int i = 0; i < n; i++){


        int r,c;

        cin >> r >> c;


        vector<vector<char>> numbs;
        for(int j = 0; j < r; j ++){
            vector<char> tvec;
            for(int k = 0; k < c; k ++){
            
                char tmp;
                cin >> tmp;

                tvec.push_back(tmp);

            }
            numbs.push_back(tvec);
        }



        bool first = true;
        for(int j = 0; j < r; j ++){
            if(first == true and count(numbs[j])){
                first = false;
                filrow(numbs[j]);
                for(int k = 0; k < j; k ++){
                    numbs[k] = numbs[j];

                }

            } else {
                filrow(numbs[j]);
            }

        }

        cout << "Case #" << i+1<< ":" << endl;
        for(auto x : numbs){
            for(auto v : x){
                cout << v;
            }
            cout << endl;
        }


    }
}
