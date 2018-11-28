#include <iostream>
#include <cstdio>
using namespace std;
pair<long long, long long> solve(long long stalls, long long people){
    if(people == 1){
        return {stalls / 2 , (stalls - 1) / 2};
    }
    if(stalls % 2 == 1 || people % 2 == 0)
        return solve(stalls / 2, people / 2);

    return solve((stalls - 1) / 2 , people / 2);
}
int main()
{
    freopen ("input.txt","r",stdin);
    freopen ("output.txt","w",stdout);

    int t;
    cin >> t;
    for(int f=1; f<=t; f++){
      long long x, y;
      cin >> x >> y;
      pair<long long, long long> p = solve(x, y);
      cout << "Case #" << f << ": " << p.first << " " << p.second << endl;
    }
    return 0;
}
