#include <bits/stdc++.h>

using namespace std;

void
Filework(void){
	freopen("blarge.in", "r", stdin);
	freopen("blarge.out", "w", stdout);
}

char s[105];
int a[105];
int len;

int
find_pos(){
    int i;
    for(i = 1; i <= len; i ++){
        if(a[i] - a[i - 1] < 0)
            return i;
    }
    return len + 1;
}

int
main(){

	Filework();

	int T;
	int t;
	int i, j;
	int pos, bpos;

    scanf("%d", &T);
    for(t = 1; t <= T; t ++){
        scanf("%s", s);
        len = strlen(s);
        for(i = 0; i < len; i ++){
            a[i + 1] = s[i] - '0';
        }
        pos = find_pos();
       // cout << pos << endl;
        if(pos > len){
            printf("Case #%d: ", t);
            printf("%s\n", s);
        }
        else{
            for(i = pos; i <= len; i ++){
                a[i] = 9;
            }
            a[pos - 1] --;
            for(i = pos - 2; i >= 1; i --){
                if(a[i] > a[i + 1]){
                    a[i + 1] = 9;
                    a[i] --;
                }
            }
            if(a[1] == 0){
                bpos = 2;
            }
            else
                bpos = 1;
            printf("Case #%d: ", t);
            for(i = bpos; i <= len; i ++){
                printf("%d", a[i]);
            }
            printf("\n");
        }
    }

return 0;
}
