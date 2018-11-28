#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
using namespace std;

int main(){
    int n;
    priority_queue <long long int> q;
    // queue <long long int> :: iterator it;
    long long int room,people,temp;
    long long int c_counter = 0;

    cin >> n;

    for (int j = 0; j < n; j++) {
        while (!q.empty()) q.pop();
        cin >> room >> people;
        c_counter++;
        q.push(room);
        for (int i = 0; i < people; i++) {

            if (i == people-1) {
              if  ( q.top() % 2 == 0 )
                  printf("Case #%lld: %lld %lld\n",c_counter,q.top() / 2,q.top() / 2-1);
              else
                  printf("Case #%lld: %lld %lld\n",c_counter,q.top() / 2,q.top() / 2);
              }
              else {
                if  ( q.top() % 2 == 0 ) {
                    q.push(q.top() / 2);
                    q.push((q.top() / 2) - 1);
                } else {
                    q.push(q.top() / 2);
                    q.push(q.top() / 2);
                }
                q.pop();
            }
        }
        // cout<<endl;
    }
}
