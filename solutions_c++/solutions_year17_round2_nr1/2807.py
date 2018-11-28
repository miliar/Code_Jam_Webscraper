#include <bits/stdc++.h>

using namespace std;

const int N = 777;


int main() {
  int tt;
  scanf("%d", &tt);
  for (int qq = 1; qq <= tt; qq++) {
    printf("Case #%d: ", qq);
    int n, d , s ,k;
    double max=0,ans,q;
   	cin>>d>>n;
   	for(int i=0;i<n;i++){
   		cin>>k>>s;
   		q=(double)(d-k)/s;
   		if(q>max)max=q;
   	}
   	ans=d/max;
    printf("%f\n", ans);
  }
  return 0;
}
