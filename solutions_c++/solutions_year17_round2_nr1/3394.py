
#include <iostream>
using namespace std;

int main(){

	int cases; cin >> cases;

	cout.precision(6);

	for(int case_num = 1; case_num <= cases; case_num++){

		cout << "Case #" << case_num << ": ";

		long double D; cin >> D;

		long int N; cin >> N;

		long double start, speed, maxspeed = 0;
		long double startcomp, speedcomp;

		cin >> start >> speed;

		for(int i = 1; i < N; i++){

			cin >> startcomp >> speedcomp;

			long double intersect_t, intersect_p;


			if(speedcomp != speed){

				intersect_t = (start - startcomp)/(speedcomp - speed);

				if(intersect_t < 0){
					if(startcomp < start){
						start = startcomp;
						speed = speedcomp;
					}
				} else {
					intersect_p = start + (speed * intersect_t);

					if(intersect_p < D){

						if(startcomp > start){

							start = startcomp;
							speed = speedcomp;

						}

					} else {

						if(startcomp < start){

							start = startcomp;
							speed = speedcomp;
						}
					}
				}
			} else {
				if(startcomp < start){

					start = startcomp;
					speed = speedcomp;
				}
			}
		}


		long double finish_t = (D - start) / speed;

		long double player_speed = D / finish_t;

		cout << fixed << player_speed << endl;

	}


}