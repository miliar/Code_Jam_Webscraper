#include <vector>
#include <stdio.h>

using namespace std;

int main() {
	
	int T;
	int counter;
	long long capturedJ;
	long long finalJ;
	long long N[150];
	long long K[150];
	
	vector<int> occ;
	vector<long long> LS;
	vector<long long> RS;
	vector<long long> minLSRS;
	vector<long long> maxLSRS;
	vector<long long> chosenMINLSRS;
	
	// number of test case
	scanf("%d", &T);
	
	for (int i = 0; i < T; i++) {
		
		// input N
		scanf("%I64d", &N[i]);
		
		// input K
		scanf("%I64d", &K[i]);
		
	}
	
	for (int i = 0; i < T; i++) {
		
		occ.clear();
		
		for (long long j = 0; j < N[i] + 2; j++) {
		
			if (j == 0 || j == N[i] + 1) {
				occ.push_back(1);
			} else {
				occ.push_back(0);
			}
		
		}
		
		for (long long idxK = 0; idxK < K[i]; idxK++) {

			LS.clear();
			RS.clear();
			minLSRS.clear();
			maxLSRS.clear();
			chosenMINLSRS.clear();
			
			for (long long j = 0; j < N[i] + 2; j++) {
				
				LS.push_back(-1);
				RS.push_back(-1);
			
				minLSRS.push_back(-1);
				maxLSRS.push_back(-1);
			
			}
		
			//printf("PERSON %I64d\n", idxK);
		
			for (long long j = 0; j < N[i] + 2; j++) {
			
				if (occ[j] == 0) {
				
					// compute LS
					counter = 0;
					for (long long k = j; k >= 0; k--) {
						if (k != j) {
							
							if (occ[k] == 0) {
								counter++;
							} else {
								break;
							}
							
						}
					}
				
					LS[j] = counter;
				
				
					// compute RS
					counter = 0;
					for (long long k = j; k < N[i] + 2; k++) {
						if (k != j) {
							
							if (occ[k] == 0) {
								counter++;
							} else {
								break;
							}
							
						}
					}
				
					RS[j] = counter;
				
				
					// compute min(LS, RS) and max(LS, RS)
					if (LS[j] < RS[j]) {
						minLSRS[j] = LS[j];
						maxLSRS[j] = RS[j];
					} else if(LS[j] > RS[j]) {
						minLSRS[j] = RS[j];
						maxLSRS[j] = LS[j];
					} else {
						minLSRS[j] = LS[j];
						maxLSRS[j] = LS[j];
					}
					
					/*
					printf("LS[%I64d]: %I64d\n", j, LS[j]);
					printf("RS[%I64d]: %I64d\n", j, RS[j]);
					
					printf("minLSRS[%I64d]: %I64d\n", j, minLSRS[j]);
					printf("maxLSRS[%I64d]: %I64d\n", j, maxLSRS[j]);
					
					printf("\n");
					*/
					
				}
			
			}
			
			// computer max min(LS, RS)
			long long MAX_MINLSRS = -1;
			for (long long j = 0; j < N[i] + 2; j++) {
				
				if (minLSRS[j] != -1) {
					
					if (MAX_MINLSRS >= minLSRS[j]) {
						MAX_MINLSRS = MAX_MINLSRS;
					} else {
						MAX_MINLSRS = minLSRS[j];
					}
					
				}
				
			}
			
			//printf("MAX_MINLSRS: %I64d\n", MAX_MINLSRS);
			
			
			// computer the number of stall having the value of MAX_MINLSRS
			counter = 0;
			capturedJ;
			
			for (long long j = 0; j < N[i] + 2; j++) {
				
				if (minLSRS[j] != -1) {
					
					if (minLSRS[j] == MAX_MINLSRS) {
						
						capturedJ = j;
						counter++;
						
						chosenMINLSRS.push_back(j);
						
					}
					
				}
				
			}
			
			
			if (counter == 1) {
				
				// choose it. DONE
				occ[capturedJ] = 1;
			
				finalJ = capturedJ;
				
			} else {
				
				// choose the one among those where max(LS, RS) is maximal
				long long MAX_MAXLSRS = -1;
				for (long long j = 0; j < chosenMINLSRS.size(); j++) {
					
					if (maxLSRS[chosenMINLSRS[j]] != -1) {
						
						if (MAX_MAXLSRS >= maxLSRS[chosenMINLSRS[j]]) {
							MAX_MAXLSRS = MAX_MAXLSRS;
						} else {
							MAX_MAXLSRS = maxLSRS[chosenMINLSRS[j]];
						}
						
					}
					
				}
				
				// computer the number of stall having the value of MAX_MINLSRS
				counter = 0;
				capturedJ;
				long long leftMostStallIdx;
				
				for (long long j = 0; j < chosenMINLSRS.size(); j++) {
					
					if (maxLSRS[chosenMINLSRS[j]] != -1) {
						
						if (maxLSRS[chosenMINLSRS[j]] == MAX_MAXLSRS) {
							
							if (counter == 0) {
								leftMostStallIdx = chosenMINLSRS[j]; 
							}
							
							capturedJ = chosenMINLSRS[j];
							counter++;
							
						}
						
					}
					
				}
				
				if (counter == 1) {
					
					// choose it. DONE
					occ[capturedJ] = 1;
					
					finalJ = capturedJ;
					
				} else {
					
					// chooset the left most stall. DONE
					occ[leftMostStallIdx] = 1;
					
					finalJ = leftMostStallIdx;
					
				}
													
			}
			
			//printf("FINAL J: %I64d\n", finalJ);
			
			if (idxK == K[i] - 1) {
				
				printf("Case #%d: %I64d %I64d\n", i+1, maxLSRS[finalJ], minLSRS[finalJ]);
				
			}
			
		}
		
	}
	
	
	
	return 0;

}