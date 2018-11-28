#include <iostream>
#include <algorithm>
#include <string>
#include <queue>

using namespace std;

int main()
{

    freopen("C-small-2-attempt0.in", "r", stdin);
    freopen("C-medium.txt", "w", stdout);


    int t;
    long long a, b;
    long long prev=0;
    long long c1,c2;

    cin >> t;
    for(int i=1;i<=t;i++){
        cin >> a >> b;
        priority_queue<long long> pq;
        for(int j=1;j<=b;j++){
            if(a%2 == 1){
                c1 = a/2;
                c2 = a/2;
            }else{
                c1 = a/2;
                c2 = a/2-1;
            }

            pq.push(c1);
            pq.push(c2);

            a = pq.top();
            pq.pop();

        }
        cout << "Case #" << i << ": " << c1 << ' ' << c2 <<'\n';
    }

    return 0;
}
