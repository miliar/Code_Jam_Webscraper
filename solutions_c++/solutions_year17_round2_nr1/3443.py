#include <iostream>
#include <cstdio>
using namespace std;

int main(){
	int t;	cin >> t;
	for(int i=0;i<t;i++){
		long double d,n;	cin >> d >> n;
		long double k[1005],s[1005];
		for(int x=0;x<n;x++)	cin >> k[x] >> s[x];
		for(int x=0;x<n;x++){
			for(int y=x;y<n;y++){
				if(k[x]<k[y]){
					int tmp = k[x];
					k[x] = k[y];
					k[y] = tmp;
					tmp = s[x];
					s[x] = s[y];
					s[y] = tmp;
				}
			}
		}

		// printf("t %d\n",i);
		// printf("d %Lf n %Lf\n",d,n);
		// for(int x=0;x<n;x++){
			
		// }

		long double max = -2147483647;
		long double time = -2147483647;
		for(int x=0;x<n;x++){
			long double tmptime, tmp;
			if(d==k[x]){
				tmptime = 0;
				tmp = s[x];
			}
			else{
				tmptime = (d-k[x])/s[x];
				tmp = d/(tmptime);
			}
			// printf("k %Lf s %Lf\n",k[x],s[x]);
			// printf("tmp %Lf tmptime %Lf\n",tmp,tmptime );
			if(tmptime > time){
				max = tmp;
				time = tmptime;
			}
			else if(tmptime == time){
				if(tmp < max){
					max = tmp;
					time = tmptime;
				}
			}
		}
		printf("Case #%d: %Lf\n",i+1, max);



		


	}
	return 0;
}