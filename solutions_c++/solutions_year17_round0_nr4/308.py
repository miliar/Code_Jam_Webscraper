 #include <iostream>
 
 #define MAXN 100
 //this is easy case
 
 //problem is equivalent to putting non-attacking rooks and non-attacking bishops on the board (independently)
 //'x' is rook, '+' is bishop, 'o' is both
 
 const char code[4] = {0,'x','+','o'};
 
 int T,N,M;
 
 int inRk[MAXN+1],outRk[MAXN+1];
 bool usedC[MAXN+1];
 
 int inBsh[2*MAXN+3], outBsh[2*MAXN+3];
 bool usedD[2*MAXN+3];
 
 
 
 int main(){
	std::cin>>T;
	for(int i=0;i<T;i++){
		
		std::cin>>N>>M;
		
		for(int j=1;j<=2*N+2;j++){
			if(j<=N){
				usedC[j]=0;
				inRk[j]=outRk[j]=0;
			}
			usedD[j]=0;
			inBsh[j]=outBsh[j]=0;
		}
		
		int count=0;
		for(int j=0;j<M;j++){
			char c;
			int R,C;	
			std::cin>>c>>R>>C;

			count++;
			if(c=='o')
				count++;


			if(c=='x' || c=='o'){
				inRk[R]=outRk[R]=C;
				usedC[C]=1;
			}

			if(c=='+' || c=='o'){
				inBsh[R+C]=outBsh[R+C]=N+1+R-C;
				usedD[N+1+R-C]=1;
			}
		}
		
		int added=0;

		int R=1,C=1;//fill in rooks
		while(R<=N && C<=N){
			if(outRk[R]>=1){
				R++;
			}else if(usedC[C]){
				C++;
			}else{
				outRk[R]=C;
				usedC[C]=1;
				count++;
				added++;
			}
		}
		
		for(int S=2;S<=2*N;S++){//fill in bishops, indexed by sum and difference

			if(outBsh[S]>=1)
				continue;
			int minD = (S<=N+1?(N+3-S):(S+1-N)) ,maxD=(S<=N+1?(N-1+S):(3*N+1-S));
			int m=minD,M=maxD;

			while(m<=2*N && usedD[m]){
				m+=2;
			}
			while(M>=0 &&usedD[M])
				M-=2;

			if(m>maxD)
				continue;
			
			if((M<N+1) || (m<N+1 && (2*N+2-m > M))){
				outBsh[S]=m;
				usedD[m]=1;
			}else{
				outBsh[S]=M;
				usedD[M]=1;
			}
			
			int D=outBsh[S];
			int R=(S+D-N-1)/2, C=(S-(D-N-1))/2;
			if(!(inRk[R]==0 && outRk[R]==C))
				added++;
			count++;
			
			
		}

		std::cout<<"Case #"<<i+1<<": "<< count <<' '<<added<<'\n';
		
		for(int R=1;R<=N;R++){//output the added rooks
			if(inRk[R]==outRk[R])
				continue;
			int C=outRk[R];
			int S=R+C,D=N+1+R-C;
			char c;
			if(outBsh[S]==D)
				c='o';
			else
				c='x';
			std::cout<<c<<' '<<R<<' '<<C<<'\n';
		}
		for(int S=2;S<=2*N;S++){//output the added bishops
			if(inBsh[S]==outBsh[S])
				continue;
			int D=outBsh[S];
			int R=(S+D-N-1)/2, C=(S-(D-N-1))/2;
			char c;
			if(inRk[R]==0 && outRk[R]==C)//already added
				continue;
			if(outRk[R]==C)
				c='o';
			else
				c='+';
			std::cout<<c<<' '<<R<<' '<<C<<'\n';
		}
	}
	return 0;
 }