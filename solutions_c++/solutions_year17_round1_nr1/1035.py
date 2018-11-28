#include <iostream>
#include <vector>
#include <tuple>

void serialize() {
  std::size_t width, height;
  std::cin >> height >> width;
  char grid[width*height];

  std::vector<std::tuple<char, std::size_t, std::size_t>> children;

  for(std::size_t v = 0; v < height; ++v) {
    for(std::size_t u = 0; u < width; ++u) {
      char c;
      std::cin >> c;
      grid[v*width + u] = c;

      if(c != '?') {
        children.push_back(std::make_tuple(c, u, v));
      }
    }
  }

  std::vector<std::tuple<char, std::size_t, std::size_t, std::size_t>> bounds;

  for(auto const &child : children) {
    char c;
    std::size_t u0, v0;
    std::size_t vlo, vhi;

    std::tie(c, u0, v0) = child;

    // try to expand up
    vhi = v0;
    for(std::size_t v = v0 + 1; v < height; ++v) {
      if(grid[v*width + u0] == '?') {
        grid[v*width + u0] = c;
        ++vhi;
      } else {
        break;
      }
    }

    // try to expand down
    vlo = v0;
    for(std::size_t v = 1; v <= v0; ++v) {
      if(grid[(v0 - v)*width + u0] == '?') {
        grid[(v0 - v)*width + u0] = c;
        --vlo;
      } else {
        break;
      }
    }

    bounds.push_back(std::make_tuple(c, u0, vlo, vhi));
  }

  for(auto const &child : bounds) {
    char c;
    std::size_t u0;
    std::size_t vlo, vhi;

    std::tie(c, u0, vlo, vhi) = child;

    // try to expand right
    for(std::size_t u = u0 + 1; u < width; ++u) {
      bool expand = true;
      for(std::size_t v = vlo; v <= vhi; ++v) {
        if(grid[v*width + u] != '?') {
          expand = false;
          break;
        }
      }
      if(expand) {
        for(std::size_t v = vlo; v <= vhi; ++v) {
          grid[v*width + u] = c;
        }
      } else {
        break;
      }
    }

    // try to expand left
    for(std::size_t u = 1; u <= u0; ++u) {
      bool expand = true;
      for(std::size_t v = vlo; v <= vhi; ++v) {
        if(grid[v*width + (u0 - u)] != '?') {
          expand = false;
          break;
        }
      }
      if(expand) {
        for(std::size_t v = vlo; v <= vhi; ++v) {
          grid[v*width + (u0 - u)] = c;
        }
      } else {
        break;
      }
    }
  }

  for(std::size_t v = 0; v < height; ++v) {
    for(std::size_t u = 0; u < width; ++u) {
      std::cout << grid[v*width + u];
    } std::cout << std::endl;
  }
}

int main(int argc, char *argv[]) {
  std::size_t num;

  std::cin >> num;

  for(std::size_t u = 1; u <= num; ++u) {
    std::cout << "Case #" << u << ':' << std::endl;
    serialize();
  }

  return 0;
}
