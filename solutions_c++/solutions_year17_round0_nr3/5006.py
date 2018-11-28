#include <iostream>
#include <queue>
 
using namespace std;


int main(void) {
    int t=0;
    cin >> t;

    for (int x=1; x<=t; x++) {
        unsigned long n;
        unsigned long k;
        cin >> n;
        cin >> k;
        priority_queue<unsigned long> q;

        q.push(n);
        for (int i =0; i < k-1; i++){
            if (!q.empty()){
                unsigned long current = q.top();
                q.pop();
                q.push(current/2);
                if (current%2==0){
                    if (current/2!=0)
                        q.push(current/2-1);
                    else 
                        q.push(current/2);
                } else {
                    q.push(current/2);
                }
            }
        }
        unsigned long min = 0;
        unsigned long max = 0;
        if (!q.empty()){
            unsigned long current = q.top();
            max = current/2;
            min = current/2;
            if ((current%2==0)&&(current!=0)){
                min--;
            }
        }

        cout << "Case #" << x << ": " << max << " " << min << endl;
        


    }
    return 0;
}