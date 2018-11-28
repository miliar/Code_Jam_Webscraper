#include<iostream>
#include<iomanip>
#include<cstdio>
#include<vector>
#include<algorithm>

# define M_PI           3.14159265358979323846

std::vector< std::vector<long double> > area; //{aporteTot,radio,altura}
std::vector<long double> noArea;// {aporte}

bool ord(long double a, long double b){
	return a > b;
}

bool ordVec(std::vector<long double> a, std::vector<long double> b){
	return a[0] > b[0];
}

int main(){
	int numCasos, pedido, numTort;
	long double radio, altura, sol;
	std::cin >> numCasos;
	for(int caso = 0; caso < numCasos; caso++){
		std::cin >> numTort >> pedido;
		
		area.clear();
		noArea.clear();	
		sol = 0;	


		for(int i = 0; i<numTort; i++){
			std::cin >> radio >> altura;
			std::vector<long double> info;
			info.push_back((altura*radio*M_PI*2)+(radio*radio*M_PI));
			info.push_back(radio);
			info.push_back(altura);
			area.push_back(info);
		}

		std::sort(area.begin(), area.end(), ordVec);

		for(int i = 0; i<pedido; i++){
			if(area.size()==0){
				sol+=noArea[0];
				noArea.erase(noArea.begin());
			} else {
				if(noArea.size()==0){
					sol+=area[0][0];
					radio=area[0][1];
					area.erase(area.begin());
					for(int j = 0; j<area.size(); j++){
						if(area[j][1]<=radio){
							noArea.push_back(area[j][2]*2*M_PI*area[j][1]);
							area.erase(area.begin()+j);
							j--;
						} else {
							area[j][0]=(area[j][1]*area[j][1]*M_PI)-(radio*radio*M_PI)+(area[j][1]*area[j][2]*2*M_PI);
						}
					}
					std::sort(area.begin(), area.end(), ordVec);
					std::sort(noArea.begin(), noArea.end(), ord);

				} else {
					if(area[0][0]>noArea[0]){
						sol+=area[0][0];
						radio=area[0][1];
						area.erase(area.begin());
						for(int j = 0; j<area.size(); j++){
							if(area[j][1]<=radio){
								noArea.push_back(area[j][2]*2*M_PI*area[j][1]);
								area.erase(area.begin()+j);
								j--;
							} else {
								area[j][0]=(area[j][1]*area[j][1]*M_PI)-(radio*radio*M_PI)+(area[j][1]*area[j][2]*2*M_PI);
							}
						}
						std::sort(area.begin(), area.end(), ordVec);
						std::sort(noArea.begin(), noArea.end(), ord);
					} else {
						sol+=noArea[0];
						noArea.erase(noArea.begin());
					}

				}
			}
		}
		std::cout << "Case #" << caso+1 << ": " << std::fixed << std::setprecision(9)<<sol << '\n';
		//std::printf("Case #%i: %Lf\n",caso+1,sol);
	}
}
