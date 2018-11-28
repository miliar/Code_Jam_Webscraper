
#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <map>
using namespace std;
#define MOD 1000000007

struct Data{
    int start, end;
    int cameron;

    Data(int x, int y, int z) : start(x), end(y), cameron(z) {
    }
};

bool compare(Data a, Data b) {
    return a.start <= b.start;
}


int testcase() {
    int sumcam[2] = {0,0};
    int ac, aj;
    cin>>ac>>aj;
    vector<Data> data;

    for (int i =0; i<ac; i++) {
    int x,y;
        cin>>x>>y;
        sumcam[1] += (y-x);
        data.push_back(Data(x,y,1));
    }
    for (int i =0; i<aj; i++) {
    int x,y;
        cin>>x>>y;
        sumcam[0] += (y-x);
        data.push_back(Data(x,y,0));
    }
    sort(data.begin(), data.end(), compare);

    multimap<int, int> myheap;
    int answer = 0;
    for (int i = 0; i<data.size()-1; i++) {
        if (data[i].cameron == data[i+1].cameron) {
            myheap.insert(make_pair(data[i+1].start - data[i].end, data[i].cameron));
        } else {
            answer ++;
        }
    }
    if (data[0].cameron == data[data.size()-1].cameron) {
        myheap.insert(make_pair(data[0].start+1440-data[data.size()-1].end, data[0].cameron));
    } else {
        answer++;
    }

    while (!myheap.empty()) {
        pair<int, int> d = *(myheap.begin());
        myheap.erase(myheap.begin());
        if (sumcam[d.second] + d.first <= 720) {
            sumcam[d.second] += d.first;
        } else {
            answer += 2;
        }
    }
    return answer;
}

int main() {
    //init();
    int t;
    cin>>t;
    for (int i = 1; i<=t; i++) {
        auto result = testcase();
        cout<<"Case #"<<i<<": "<<result<<endl;
    }
    return 0;
}

