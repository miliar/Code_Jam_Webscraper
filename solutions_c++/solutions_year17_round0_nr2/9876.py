#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <set>
#include <cmath>
#include <cstdlib>

using namespace std;


int main() {
        int cases=0;
        cin >> cases;

        for(int casesIter=0;casesIter<cases;casesIter++) {
                char s[30];
		char res[30] = {'\0'};
                scanf("%s\n", s);


		if(strlen(s) == 1) {
			printf("Case #%d: %s\n",casesIter+1, s);
			continue;
		}
		bool changed = false;

		int i;
                for(i=0;i< strlen(s);i++)
                {
			if(changed == true ) {
				res[i] = '9';
			}
			else if(s[i] > s[i+1] && ( i < (strlen(s) -1) )) {
				res[i] = s[i]-1;
				int temp = i;
				while (temp != 0 && res[temp-1] > res[temp]) {
					res[temp-1] = res[temp-1] - 1;
					temp--;
				}
				i = temp;
				changed = true;
			}
			else {
				res[i] = s[i];
			}
			
                }
		res[i] = s[i];
	
		if(res[0] == '0') {
                	printf("Case #%d: %s\n",casesIter+1, &res[1]);
		} else {
			printf("Case #%d: %s\n",casesIter+1, &res[0]);
		}

        }

        return 0;
}
