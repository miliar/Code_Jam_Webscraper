#include <stdio.h>

int main() {
  int t;
  char s[100];
  int m;
  bool is = true;
  int answer = 0;

  FILE *fp, *wp;

  fp = fopen("A-small-attempt3.in", "r");
  wp = fopen("output.txt", "w");
  fscanf(fp, "%d", &t);

  	for (int i = 1; i <= t; ++i) {
    	fscanf(fp, "%s %d", s, &m);
    	//printf("%s\n", s);
	    for(int j = 0; s[j + m - 1] != '\0'; j++){
	    	if(s[j] == '-'){
	    		//printf("test\n");
	    		answer += 1;
	    		for(int k = 0; k < m; k++)
	    		{
	    			//printf("before: %s\n", s);
	    			if(s[j + k] == '+')
	    			{
	    				s[j + k] = '-';
	    			}
	    			else
	    			{
	    				s[j + k] = '+';
	    			}
	    			//printf("after: %s\n", s);
	    		}
	    	}
	    }
	    //printf("%s\n", s);
	    for(int j = 0; j < s[j] != '\0'; j++){
	    	if(s[j] == '-'){
	    		is = false;
	    	}
                s[j] = '\0';
	    }

	    if(is)
	    {
	    	fprintf(wp, "Case #%d: %d\n", i, answer);
	    }
	    else{
	    	fprintf(wp, "Case #%d: IMPOSSIBLE\n", i);
	    }
	   	answer = 0;
	   	is = true;         
	  }
  fclose(fp);
  fclose(wp);
  return 0;
}
