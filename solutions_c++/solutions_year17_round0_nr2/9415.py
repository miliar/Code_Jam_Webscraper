#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string.h>

using namespace std;



/* Global Variables*/    
    int pos, preNum, num;
    char tmp[20], resultStr[20];
/*---------*/  




int findTidy()
{
    int i = 0, result = 0, stop;
    int size = strlen(tmp);
       
    preNum = -1;
    stop = 0;
    memset(resultStr, 0, sizeof(resultStr));
       
    for(i = 0; i < size; i ++)
    {
        num = tmp[i] - '0';
        if (num > preNum && stop == 0)
        {
        	pos = i;
        	resultStr[pos] = tmp[i];
        }
        	
    	if(num < preNum)
    		stop = 1;
    		
    	preNum = num;
        
    }
    
    if (stop == 0)
    	strcpy(resultStr, tmp);
    else
    {
	
		if(resultStr[pos] == '1')
		{
		    for(i = pos; i < size-1; i ++)
		    {
		    	resultStr[i] = '9';
			}
		}	
		else
		{
			resultStr[pos] = resultStr[pos] - 1;
			for(i = pos+1; i < size; i ++)
		    {
		    	resultStr[i] = '9';
			}
		}
	}
	return 0;
    
}


int main(int argc, char *argv[])
{

    char *inFileName = "B-small-attempt0.in";
    char *outFileName = "B-small-attempt0.out";
    int i, j, k, l, m;
    int group;
    int ans1, ans2;
/* Local Variables*/    
    //int A, N;
    int result;
/*---------*/    
    FILE * pInFile, *pOutFile;
	char * i2str = "abcdefghijklmnopqrstuvwxyz";     

    if((pInFile = fopen(inFileName, "r")) == NULL)
          printf("error open file\n");

    if((pOutFile = fopen(outFileName, "w")) == NULL)
          printf("error open file\n");

	
    fscanf(pInFile, "%d", &group);
    printf("group %d\n", group);
    for(i =0; i< group; i++)
    {
          fscanf(pInFile, "%s\n", tmp);
          printf("%s\n", tmp);
          findTidy();
          
          fprintf(pOutFile, "Case #%d: %s\n", i+1, resultStr);
          
    }
        
    fclose(pInFile);
    fclose(pOutFile);
    
    system("PAUSE");
    return EXIT_SUCCESS;
}



