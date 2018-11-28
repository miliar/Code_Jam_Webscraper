#include<iostream>
#include<vector>
using namespace std;

typedef long long ll;

bool all(const vector<bool>& v) {
    for( bool b : v) {
        if(b==false) return false;
    }
    return true;
}
int countPancakes(const vector<bool>& v) { // count down to 0
    int count = v.size();
    for(bool b : v ) { if (b) count--; }
    return count;
}

int flipPancakes(vector<bool>& v, int k, int pos) {
    int numberFlippedTrue = 0;
    for(int i = pos; i < pos+k; ++i) {
        bool b=v[i];
        if (b) {
            v[i]= !b;
            numberFlippedTrue--;
        } else { 
            v[i]=!b; 
            numberFlippedTrue++;
        }
    }
    //cerr << "num flipped: " << numberFlippedTrue << "\n";
    return numberFlippedTrue;
}
string to_string(vector<bool>& v) {
    string s= "v "; 
    for(bool b: v) {
        s+=(b)?"1":"0";
    }
    return s;
}

int main() {
    std::ios::sync_with_stdio(false);
	int n, c =1, k;
    cin >> n;

    while(n--) {
        string spancakes;
        vector<bool> pancakes;
        pancakes.clear();
        int numFlips=0;
        cin >> spancakes >> k;
        //cerr << "spancakes " << spancakes << "\n";
        //cerr << "spancakes length " << spancakes.length() << "\n";
        for(char c: spancakes) {
            if(c=='+') pancakes.push_back(true);
            else if(c=='-') pancakes.push_back(false);
        }
        int count;
        

        count = countPancakes(pancakes);
        if(count ==0) {
            cout << "Case #" << c++ <<": " << numFlips << "\n";
            continue;
        }
        //cerr << to_string(pancakes) << "\n";
        //cerr << count << "\n";

        for(int i =0; i <= pancakes.size()-k; i ++) {
            if(!pancakes[i]) {
                int change =flipPancakes(pancakes, k, i);
                numFlips++;
                count-= change; 
                //cerr << to_string(pancakes) << "\n";
                //cerr << count << "\n";
                
                if(count==0) break;
            }   
        }
        if(count>0) {
            cout << "Case #" << c++ << ": " << "IMPOSSIBLE\n";
        }
        else cout << "Case #" << c++ <<": " << numFlips << "\n";
    }
    return 0;    
}
