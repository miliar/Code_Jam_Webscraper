#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <math.h>
#include <sstream>
#include <cstring>
#include <climits>
#include <ctype.h>

using namespace std;


bool ascend(int n){
int p = n%10;
n/=10;
while(n > 0){
    if(n%10 > p)return false;
    p = n%10;
    n/=10;
}
return true;
}

int main()
{
 freopen("input.in","r",stdin);
 freopen("output.out","w",stdout);

int t,n;
cin >> t;
for(int i = 1 ; i <= t;i++){
cin >> n;
while(true){
    if(ascend(n))break;
n--;
}
    cout <<"Case #"<<i<<": "<<n<<endl;
}

    return 0;
}
