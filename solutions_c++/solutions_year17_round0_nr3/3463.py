#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <queue>

using namespace std;
typedef long long ll;

int main(){
    ifstream infile("in.txt");
    ofstream outfile("out.txt");

    int t; infile>>t;
    for (int h=0; h<t; h++){
        outfile<<"Case #"<<h+1<<": ";
        ll n, k;
        infile>>n>>k;
        priority_queue<int> splits;
        splits.push(n);
        int i=1;
        while (i<k){
            int x=splits.top();
            splits.pop();
            x--;
            if (x%2==0){
                splits.push(x/2);
                splits.push(x/2);
            }
            else {
                splits.push((x-x%2)/2+1);
                splits.push((x-x%2)/2);
            }
            i++;
        }
        int v=splits.top();
        v--;
        if (v%2==0){
            outfile<<(v/2)<<" ";
            outfile<<(v/2)<<endl;
        }
        else {
            outfile<<((v-v%2)/2+1)<<" ";
            outfile<<((v-v%2)/2)<<endl;
        }
        cout<<h<<endl;
    }
}









