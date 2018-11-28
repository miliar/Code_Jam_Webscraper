#include <iostream>
#include <vector>

double steed2(int dist, int size){
	std::vector<int> startingPoint(size);
	std::vector<int> speed(size);
	std::vector<double> endTime(size);

	for(int i=0;i<size;++i){
		std::cin >> startingPoint[i] >> speed[i];
		endTime[i]=((double)(dist-startingPoint[i]))/speed[i];
	}

	double maxTime=endTime[0];

	for(int i=1;i<size;++i){
		if(endTime[i]>maxTime)
			maxTime=endTime[i];
	}

	return dist/maxTime;
}

void contest(){
	int distance, horses;
	std::cin>>distance>>horses;

	
	std::cout<< std::fixed<<steed2(distance, horses);
}

int main(){
	int n;
	std::cin>>n;
	++n;
	for(int i=1;i<n;++i){
		std::cout<<"Case #"<<i<<": ";
		contest();
		std::cout<<'\n';
	}

	return 0;
}