#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <string>
#include <iostream>
using namespace std;

int main() {
unsigned long long  t, i, j, k, l, m;
freopen("in.in","r+",stdin);
freopen("out.out","w+",stdout);
cin >> t;
for (i = 1; i <= t; i++) {
unsigned long long num,j,ans, quo;
cin >> num;
j = num;
for (;j>0;j--) {
quo = j;
ans =0;

while(1) {
int rem = quo % 10;
quo = quo/10;
if(!quo) {
                ans = j;
                break;
        }
int rem_1 = quo % 10;  

if (rem < rem_1)
	break;
}
if (ans)
	break;
}
	/*answer */
	cout << "Case #" << i  <<": " << ans << endl;
}
}

