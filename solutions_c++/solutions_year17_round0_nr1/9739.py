#include<iostream>
#include<vector>
#include<queue>
#include<string>

using namespace std;

int count_pancake(string pancakes) {
    int count = 0;
    for(int i = 0; i < pancakes.length(); i++) {
        if (pancakes[i] == '-') count++;
    }
    return count;
}

bool ok_pancake(string pancakes) {
    for(int i = 0; i < pancakes.length(); i++) {
        if (pancakes[i] == '-') return false;
    }
    return true;
}

bool visited_node(vector<string> visited_pancake, string pancakes) {
    for(int i=0; i<visited_pancake.size(); i++){
        if (visited_pancake[i] == pancakes) return true;
    }
    return false;
}

string flip_pancake(string pancakes, int start, int f_size) {
    for(int i = start; i < (start + f_size); i++){
        if (i == pancakes.length()) break;
        if(pancakes[i] == '-') pancakes[i] = '+';
        else pancakes [i] = '-';
        
    }
    return pancakes;
}

class ComparePair {
public:
    bool operator()(pair<string, int > n1, pair<string, int> n2) {
        return (count_pancake(n1.first)+n1.second)>(count_pancake(n2.first)+n2.second);
    }
};


int main(){
    pair<string, int > foo;
    int t, flipper;
    string pancakes;
    
    cin >> t;

    for (int i = 1; i <= t; ++i){
        bool got_res = true;
        int cost = 0;
        priority_queue<pair<string,int>,vector<pair<string,int> >,ComparePair> pq;
        vector<string> visited_pancake;

        cin >> pancakes >> flipper;
        
        foo = make_pair(pancakes, cost);
        pq.push(foo);
        while(count_pancake(pq.top().first) > 0) {
            pancakes = pq.top().first;
            int cur_cost =  pq.top().second;
            ++cur_cost;
            pq.pop();
            if (visited_node(visited_pancake, pancakes)){
                if (pq.size() != 0) continue;
                got_res = false;
                break;
            }
            // cout << pancakes << ", " << cur_cost << endl;
            visited_pancake.push_back(pancakes);
            
            for(int i = 0; i < (pancakes.length()-flipper+1); i++) {
                foo = make_pair(flip_pancake(pancakes,i,flipper), cur_cost);
                pq.push(foo);
            }
            
        }
        if(got_res) cout << "Case #" << i << ": " << pq.top().second << endl;
        else cout << "Case #" << i << ": IMPOSSIBLE" << endl;
    }
}
