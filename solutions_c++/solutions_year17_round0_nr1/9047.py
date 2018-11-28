#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string.h>

using namespace std;



/* Global Variables*/    
    int numBase;
/*---------*/  




int count()
{
    int i = 0, result = 0, mask = 0, numTmp, curNum = numBase;
    int maskTmp = mask;
	
	if(curNum == 0)
		return 0;    
        
    for(i = 1; 1; i ++)
    {
        numTmp = curNum;
		
		while(numTmp>0)
		{
			mask |= 1 << (numTmp%10);
			numTmp /= 10;
		}
		
		if(maskTmp != mask)
			printf("%d val %d mask %x\n", i, curNum, mask);
		maskTmp = mask;
		
		if(mask == 0x3ff)
			return curNum;
		
		curNum += numBase;
    }
}


int main(int argc, char *argv[])
{

    char *inFileName = "A-small-attempt0.in";
    char *outFileName = "A-small-attempt0.out";
    int i, j, k;
    int group;
    int ans1, ans2;
/* Local Variables*/    
    //int A, N;
    int result;
/*---------*/    
    FILE * pInFile, *pOutFile;
    

    if((pInFile = fopen(inFileName, "r")) == NULL)
          printf("error open file\n");

    if((pOutFile = fopen(outFileName, "w")) == NULL)
          printf("error open file\n");


    fscanf(pInFile, "%d", &group);
    printf("group %d\n", group);
    for(i =0; i< group; i++)
    {
          fscanf(pInFile, "%d\n", &numBase);
          printf("%d\n", numBase);
          result = count();
          
          if(result == 0)
          	fprintf(pOutFile, "Case #%d: INSOMNIA\n", i+1);
          else
          	fprintf(pOutFile, "Case #%d: %d\n", i+1, result);
    }
        
    fclose(pInFile);
    fclose(pOutFile);
    
    system("PAUSE");
    return EXIT_SUCCESS;
}



