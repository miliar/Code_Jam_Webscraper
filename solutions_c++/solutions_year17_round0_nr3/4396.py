#include <algorithm>
#include <iostream>
#include <map>

std::pair<unsigned int, unsigned int> resolveBathroomProblem(int nbRoom, int nbPeople) {
	std::map<unsigned int, unsigned int> roomLeft;
	roomLeft[nbRoom] = 1;
	int nb = 0;
	while (nb < nbPeople) {
		const unsigned int max = std::max_element(roomLeft.begin(), roomLeft.end())->first;
		while (roomLeft[max] > 0 && nb < nbPeople)
		{
			if ((max - 1) % 2 == 0) {				
				roomLeft[(max - 1) / 2] += 2;
			} else {
				roomLeft[(max - 1) / 2] += 1;
				roomLeft[(max - 1) / 2 + 1] += 1;
			}
			roomLeft[max] -= 1;
			nb++;
		}
		roomLeft.erase(max);
		if (nb == nbPeople) {
			if ((max - 1) % 2 == 0)
				return (std::pair<unsigned int, unsigned int>((max - 1) / 2, (max - 1) / 2));
			else
				return (std::pair<unsigned int, unsigned int>((max - 1) / 2 + 1, (max - 1) / 2));
		}
	}
}

int main() {
	int nbTest;
	std::cin >> nbTest;
	for (int i = 1; i <= nbTest; i++)
	{
		int nbRoom;
		int nbPeople;
		std::cin >> nbRoom >> nbPeople;
		std::pair<int, int> solution = resolveBathroomProblem(nbRoom, nbPeople);
		std::cout << "Case #" << i << ": " << solution.first << " " << solution.second << std::endl;
	}
}