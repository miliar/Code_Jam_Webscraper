#include <cstdio>
#include <cstring>
using namespace std;
char a[100]; 
int num[100];
bool used[10];
int main(){
	int t;
	scanf("%d",&t);
	for(int jizz = 1;jizz <= t;++jizz){
		scanf("%s",a);
		int len = strlen(a);
		int kind = 0;
		int pos = -1;
		for(int i = 0;i < len;++i){
			num[i] = a[i] - '0';
			if(!used[num[i]]){
				kind++;
				pos = i;
				used[num[i]] = 1;
			} 
		} 
		if(kind == 2 && pos == len - 1 && num[len - 1] < num[0]){
			num[0]--;
			printf("Case #%d: ",jizz);
			if(num[0] != 0) printf("%d",num[0]);
			for(int i = 1;i < len;++i) printf("9");
			printf("\n");
		}
		else{
			pos = -1;
			for(int i = 0;i < len;++i){
				if(num[i] > num[i + 1] && i + 1 < len){
					pos = i;
					num[i]--;
					break;
				}
			}
			printf("Case #%d: ",jizz);
			if(pos != -1){
				if(num[0] != 0) printf("%d",num[0]);
					for(int i = 1;i < len;++i){
					if(i > pos) printf("9");
					else printf("%d",num[i]);
				}
			}
			else for(int i = 0;i < len;++i) printf("%d",num[i]);
			printf("\n");
		}
		memset(used,0,sizeof(used));
		memset(a,0,sizeof(a));
		memset(num,0,sizeof(num));
	}
	return 0;
}