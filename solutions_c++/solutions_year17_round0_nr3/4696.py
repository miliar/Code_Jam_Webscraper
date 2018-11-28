
// Kasimir Tanner 2017
#include <iostream>
#include <vector>
#include <string>
#include <set>

using namespace std;

typedef long long int llint;
typedef unsigned long long int ullint;


pair<ullint,ullint> getNext(ullint x){
    if(x == 0)return make_pair(0,0);
    ullint high = x/2;
    ullint low = high;
    if(x % 2 == 0)low--;
    //cout << "Next: " << high << " " << low << "\n";
    return make_pair(low,high);
}
void print_set(multiset<pair<ullint,ullint> > x){
    cout << "Set\n";
    for(auto i: x){
        cout << i.first << " " << i.second << "\n";
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    ullint T;
    cin >> T;
    
    for(ullint t = 0;t< T;t++){

        multiset<pair<ullint,ullint> > choice;

        ullint N,K;
        cin >> N >> K;

        choice.insert(make_pair(0,N));

        for(ullint i = 0;i<K;i++){
            //print_set(choice);
            pair<ullint,ullint> next = *choice.rbegin();
            //cout << i << ": " << next.second << " " << next.first << "\n";
            if(next.second == 0)break;
            choice.insert(getNext(next.first));
            choice.insert(getNext(next.second));
            choice.erase(choice.find(next));
        }

        pair<ullint,ullint> next = *choice.rbegin();
        cout << "Case #" << t+1 << ": " << next.second << " " << next.first << "\n";

    }
    return 0;
}