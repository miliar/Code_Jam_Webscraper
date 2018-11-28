#include <stdio.h>

#include <vector>

using namespace std;

int findMin(int min[],int N, int &k) {

  int m = min[0];
  k = 0;
  for (int j = 1; j < N; j++) {
    if (min[j] < m) {
      m = min[j];
      k = j;
    }
  }
  return m;
}


int findMax(int min[],int N, int &k) {

  int m = min[0];
  k = 0;
  for (int j = 1; j < N; j++) {
    if (min[j] > m) {
      m = min[j];
      k = j;
    }
  }
  return m;
}

int main() {

  int T;

  scanf("%d",&T);
  
  for (int t = 1; t <= T; t++) {

    int kits = 0;


    int N,P;

    int amount[100];
    
    vector<int> packets[100];

    scanf("%d %d",&N,&P);

    for (int i = 0; i < N; i++) {
      scanf("%d",&amount[i]);
    }

    int firstUnused[100];
    for (int i = 0; i < N; i++) {      
      for (int j = 0; j < P; j++) {
	int g;
	scanf("%d",&g);
	packets[i].push_back(g);
      }
      sort(packets[i].begin(),packets[i].end());
      firstUnused[i] = 0;
    }
    bool done = false;

    while(done == false) {
      
      // compute, for each unused ingredient, how many portions we can make;
      int min[100];
      int max[100];

      for (int i =0; i < N; i++) {
	int weight = packets[i][firstUnused[i]];
	
	
	
	min[i] = ((double)weight ) / (1.1 * (double) amount[i]); 
	
	if (min[i] * (1.1 * (double) amount[i]) < (double)weight*0.9999999999) {
	  min[i]++;
	}
		
	max[i] = ((double)weight ) / (0.9 * (double) amount[i]); 
	if (max[i] < min[i]) {
	  min[i] = 0;
	  max[i] = 0;
	}
	//printf("Weight = %d - amount = %d\n",weight,amount[i]);
	//printf("Res %d: min = %d, max = %d\n",i,min[i],max[i]);
      }
      int k;
      int l;
      int maxmin = findMax(min,N,k);
      int minmax = findMin(max,N,l);

      //printf("Max mins = %d for resource %d\n",maxmin,k);
      //printf("Min maxs = %d for resource %d\n",minmax,l);
      
      
      if ((minmax >= maxmin) && ( minmax != 0 )) {
	// Can make one more kit;
	//printf("Make kit: \n");
	kits++;
	for (int i =0; i < N; i++) {
	  //printf("Using %d - %d\n",i,firstUnused[i]);
	  firstUnused[i]++;
	  if (firstUnused[i] >= P) {
	    done = true;
	  }
	  
	}
      }
      else {
	// minmax needs to be discarded;
	//printf("Discarding resource %d at pos %d\n",l,firstUnused[l]);
	firstUnused[l]++;
	if (firstUnused[l] >= P) {
	  done = true;
	}
	
      }

      
    }
    


    printf("Case #%d: %d\n",t,kits);



  }
    
  


}
