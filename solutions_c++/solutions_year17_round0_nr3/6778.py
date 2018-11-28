#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <string>
#include <queue>
#include <cmath>
#include <iomanip>
#include <set>
#include <map>
#include <queue>
#include <stack>
using ll = long long;
//#include <bits/stdc++.h>
using namespace std;
long long zero,cases,rooms,people,rem;
pair<long long,long long>emptypair;
vector<long long>emptyvec;
priority_queue<long long>pq;
vector<pair<ll,ll> >solutions;



int main() {
    //freopen("C:\\Users\\arijordan\\Downloads\\C-small-2-attempt0.in", "r+", stdin);
    //freopen("C-small-1-attempt1 (1).txt", "r", stdin);
    //freopen("C:\\Users\\arijordan\\Downloads\\C-small-2-attempt0out.txt", "w", stdout);
    //freopen("myfilehere4.txt", "w", stdout);
    printf ("This sentence is redirected to a file.");
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout<<setprecision(10);
    cin>> cases;
    for (int i=0; i<cases; i++) {
        cin>>rooms>>people;
        pq.push(rooms);
        for (int j=0; j<people-1; j++) {
            rem=pq.top();
            pq.pop();
                pq.push(rem/2);
            pq.push((rem-1)/2);
        }
        emptypair.first=pq.top()/2;
        emptypair.second=(pq.top()-1)/2;
        solutions.push_back(emptypair);
        while (!pq.empty()) {
            pq.pop();
        }
    }
    for (int s=0; s<solutions.size(); s++) {
        cout<<"case #"<<s+1<<": "<<solutions.at(s).first<<" "<<solutions.at(s).second<<"\n";
    }

    return 0;
}
