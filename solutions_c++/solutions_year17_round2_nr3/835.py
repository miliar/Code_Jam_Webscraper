
#include <iostream>
#include <iomanip>
using namespace std;

typedef long long ll;

int no_cases;
int N, Q;

ll endurance[101], ei;
int speed[101], si;
ll d[101][101], dij;
int uk, vk;

double ans[101];

double calculate(ll remain_kilo, int horse_speed, int curr){
	if (remain_kilo==0 && horse_speed==0){
		//starting position curr=1
		return 1.0*d[curr][curr+1]/speed[curr]+calculate(endurance[curr]-d[curr][curr+1], speed[curr], curr+1);
	}
	if (curr==vk){
		return 0;
	}

	int curr_speed=horse_speed;
	ll curr_endurance=remain_kilo;

	int change_speed=speed[curr];
	ll change_endurance=endurance[curr];

	if (curr_endurance<d[curr][curr+1]){
		//change horse
		return 1.0*d[curr][curr+1]/change_speed+calculate(change_endurance-d[curr][curr+1], change_speed, curr+1);
	}

	if (change_endurance<d[curr][curr+1]){
		//no change
		return 1.0*d[curr][curr+1]/curr_speed+calculate(curr_endurance-d[curr][curr+1], curr_speed, curr+1);
	}

	if (curr_speed>=change_speed && curr_endurance>=change_endurance){
		//no change
		return 1.0*d[curr][curr+1]/curr_speed+calculate(curr_endurance-d[curr][curr+1], curr_speed, curr+1);
	}

	if (curr_speed<=change_speed && curr_endurance<=change_endurance){
		//change
		return 1.0*d[curr][curr+1]/change_speed+calculate(change_endurance-d[curr][curr+1], change_speed, curr+1);
	}

	//non trivial
	double rta=1.0*d[curr][curr+1]/curr_speed+calculate(curr_endurance-d[curr][curr+1], curr_speed, curr+1);
	double rtb=1.0*d[curr][curr+1]/change_speed+calculate(change_endurance-d[curr][curr+1], change_speed, curr+1);
	if ( rta<rtb )
		return rta;
	else
		return rtb;



}

double solve(){
	//uk=1, vk=N
	double rt=calculate(0, 0, 1);//uk=1
	return rt;

}

int main(){
	cin>>no_cases;
	cout<<fixed<<setprecision(8);
	for (int caseID=1; caseID<=no_cases; caseID++){
		cin>>N>>Q;
		for (int i=1; i<=N; i++){
			cin>>ei>>si;
			endurance[i]=ei;
			speed[i]=si;
		}
		for (int i=1; i<=N; i++){
			for (int j=1; j<=N; j++){
				cin>>dij;
				d[i][j]=dij;
			}
		}
		cout<<"Case #"<<caseID<<": "; 
		for (int i=0; i<Q; i++){
			cin>>uk>>vk;
			double rt=solve();

			cout<<rt<<" ";
		}
		cout<<endl;

	}
}