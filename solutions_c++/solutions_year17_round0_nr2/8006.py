#include <iostream>
#include <fstream>

int main(int argc, char *argv[])
{
  if (argc != 2)
    return 1;
  std::ifstream in(argv[1]);
  std::ofstream out("output.out");
  std::string token;
  in >> token;
  int t = std::stoi(token);
  for (int row_idx = 1; row_idx <= t; row_idx++)
    {
      std::string nb;
      in >> nb;
      // BEGIN
      out << "Case #" << row_idx << ": ";
      if (nb.size() < 2)
	out << nb;
      else
	{
	  std::string result;
	  auto apply_idx = nb.rbegin();
	  for (auto it = nb.rbegin(); it != nb.rend() - 1; it++)
	    {
	      if (*it < *(it + 1))
		apply_idx = it + 1;
	      if (*it == *(it + 1) && apply_idx != nb.rbegin())
		apply_idx = it + 1;
	    }
	  for (auto it = nb.rbegin(); it != apply_idx; it++)
	    result.insert(result.begin(), '9');
	  if (apply_idx != nb.rbegin())
	    {
	      result.insert(result.begin(), *apply_idx - 1);
	      for (auto it = apply_idx + 1; it != nb.rend(); it++)
		result.insert(result.begin(), *it);
	      if (result[0] == '0')
		result.erase(result.begin());
	      out << result;
	    }
	  else
	    out << nb;
	}
      out << std::endl;
      // END
    }
  in.close();
  out.close();
  return 0;
}
